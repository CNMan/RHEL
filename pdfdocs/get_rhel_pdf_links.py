import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_rhel_pdf_links_for_versions(start_ver=4, end_ver=10):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')          # 无头模式
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    
    # 📌 显式指定您的 Chrome 安装路径
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    options.binary_location = chrome_path
    
    print(f"正在初始化 Chrome 浏览器 (路径: {chrome_path})...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # 循环遍历请求的每一个大版本（RHEL 4 至 10）
        for version in range(start_ver, end_ver + 1):
            base_url = f"https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/{version}"
            txt_filename = f"rhel{version}pdfdoc.txt"
            
            print(f"\n🚀 [RHEL {version}] 正在发起抓取目标页面: {base_url}")
            
            try:
                driver.get(base_url)
                
                # 等待页面核心 a 标签渲染完成
                WebDriverWait(driver, 12).until(
                    EC.presence_of_element_located((By.TAG_NAME, "a"))
                )
                time.sleep(2) # 页面底图和复杂DOM加载缓冲时间
                
                # 模拟滚动页面，迫使前端 Ajax 触发所有隐藏或懒加载的子卡片
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1.5)
                
                links = driver.find_elements(By.TAG_NAME, "a")
                pdf_urls = set()
                
                # 遍历页面上的链接进行精准路径重构
                for link in links:
                    try:
                        href = link.get_attribute("href")
                        if not href:
                            continue
                        
                        # 兼容过滤老版本和新版本的匹配逻辑（检测对应版本的文档目录名路径与 /html/ 标志）
                        version_flag = f"/documentation/red_hat_enterprise_linux/{version}"
                        if version_flag in href and "/html/" in href:
                            match = re.search(r'/html/([^/]+)', href)
                            if match:
                                book_slug = match.group(1)
                                if book_slug in ["index", ""] or not book_slug.strip():
                                    continue
                                
                                # 红帽统一标准格式化命名：
                                # 拆分下划线，如果段落全部是数字版号（如 10.2 / 7.9）不转化大写，其余单词首字母大写
                                words = book_slug.split('_')
                                formatted_words = []
                                for i, word in enumerate(words):
                                    if i == 0 and re.match(r'^\d+(\.\d+)?$', word):
                                        formatted_words.append(word)
                                    else:
                                        formatted_words.append(word.capitalize())
                                
                                file_title = "_".join(formatted_words)
                                
                                # 根据官方规律完美还原 PDF CDN 下载路径
                                pdf_file_url = f"https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/{version}/pdf/{book_slug}/Red_Hat_Enterprise_Linux-{version}-{file_title}-en-US.pdf"
                                pdf_urls.add(pdf_file_url)
                    except Exception:
                        continue
                
                # 写入文本数据中（如果由于生命周期绝版导致 RHEL 早期版本无此路径，则生成空文件或少链接文件）
                sorted_links = sorted(list(pdf_urls))
                with open(txt_filename, "w", encoding="utf-8") as f:
                    for link_item in sorted_links:
                        f.write(link_item + "\n")
                        
                print(f"💾 [RHEL {version}] 抓取完成！共收集到 {len(sorted_links)} 个有效 PDF 直链，已成功存入本地: {txt_filename}")
                
            except Exception as page_err:
                print(f"⚠️ 抓取 RHEL {version} 文档主页时遭遇错误（可能该旧版本已迁移到其他归档池）: {page_err}")
                # 保证即使报错也会生成对应的文本文件
                with open(txt_filename, "w", encoding="utf-8") as f:
                    f.write(f"# 无法获取 RHEL {version} 数据或没有有效的 PDF 文件\n")
                continue
                
    finally:
        driver.quit()
        print("\n✨ 所有版本批量提取完成，浏览器会话已安全关闭。")

if __name__ == "__main__":
    get_rhel_pdf_links_for_versions(4, 10)
