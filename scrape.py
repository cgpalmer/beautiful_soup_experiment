import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import os
import time
start = time.time()
print("starting")

# # List of iframe links below
iframes = ["https://social-blog.wix.com/custom-feed-widget?pageId=ixlsv&compId=comp-kbwc8pql&viewerCompId=comp-kbwc8pql&siteRevision=2588&viewMode=site&deviceType=desktop&locale=en&tz=America%2FNew_York&width=920&height=3314&instance=ui6twEcmgE2Seo_QrA3iefKVQB0OvBzDMyJNUCCajnU.eyJpbnN0YW5jZUlkIjoiNTQ0Y2FmYzAtMTAwOC00NDllLWExMjktODA4YWQ4MDhiMzJjIiwiYXBwRGVmSWQiOiIxNGJjZGVkNy0wMDY2LTdjMzUtMTRkNy00NjZjYjNmMDkxMDMiLCJtZXRhU2l0ZUlkIjoiMDg4MDljZDctNDhiMy00MmZiLWE0NzAtNTI0YTBkMWZiM2RkIiwic2lnbkRhdGUiOiIyMDIxLTAyLTE0VDIxOjQ5OjAzLjk3NVoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjIzMTRiZmVjLWQ4NjYtNDYyNC1hNzU5LTg2MWNiMGQ5MDc2ZSIsImJpVG9rZW4iOiI1Y2NjMzMxNy01OGJiLTA2NjUtMDU1OS1kMmMwZDUxNzAwZjEiLCJzaXRlT3duZXJJZCI6ImM2NDc1ZmVhLTllNTEtNGE2MS04NjM2LTkyNjVmNDM4MjcwMyJ9&currency=GBP&currentCurrency=GBP&vsi=908a90f0-af79-41da-9590-29612c72b3ca&commonConfig=%7B%22brand%22%3A%22wix%22%2C%22bsi%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C4%22%2C%22BSI%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C4%22%7D",
            "https://social-blog.wix.com/custom-feed-widget?pageId=o03vp&compId=comp-ket2ztx1&viewerCompId=comp-ket2ztx1&siteRevision=2588&viewMode=site&deviceType=desktop&locale=en&tz=America%2FNew_York&width=993&height=607&instance=ui6twEcmgE2Seo_QrA3iefKVQB0OvBzDMyJNUCCajnU.eyJpbnN0YW5jZUlkIjoiNTQ0Y2FmYzAtMTAwOC00NDllLWExMjktODA4YWQ4MDhiMzJjIiwiYXBwRGVmSWQiOiIxNGJjZGVkNy0wMDY2LTdjMzUtMTRkNy00NjZjYjNmMDkxMDMiLCJtZXRhU2l0ZUlkIjoiMDg4MDljZDctNDhiMy00MmZiLWE0NzAtNTI0YTBkMWZiM2RkIiwic2lnbkRhdGUiOiIyMDIxLTAyLTE0VDIxOjQ5OjAzLjk3NVoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjIzMTRiZmVjLWQ4NjYtNDYyNC1hNzU5LTg2MWNiMGQ5MDc2ZSIsImJpVG9rZW4iOiI1Y2NjMzMxNy01OGJiLTA2NjUtMDU1OS1kMmMwZDUxNzAwZjEiLCJzaXRlT3duZXJJZCI6ImM2NDc1ZmVhLTllNTEtNGE2MS04NjM2LTkyNjVmNDM4MjcwMyJ9&currency=GBP&currentCurrency=GBP&vsi=908a90f0-af79-41da-9590-29612c72b3ca&commonConfig=%7B%22brand%22%3A%22wix%22%2C%22bsi%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C8%22%2C%22BSI%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C8%22%7D",
            "https://social-blog.wix.com/custom-feed-widget?pageId=irlo9&compId=comp-kcazzhz0&viewerCompId=comp-kcazzhz0&siteRevision=2588&viewMode=site&deviceType=desktop&locale=en&tz=America%2FNew_York&width=920&height=290&instance=ui6twEcmgE2Seo_QrA3iefKVQB0OvBzDMyJNUCCajnU.eyJpbnN0YW5jZUlkIjoiNTQ0Y2FmYzAtMTAwOC00NDllLWExMjktODA4YWQ4MDhiMzJjIiwiYXBwRGVmSWQiOiIxNGJjZGVkNy0wMDY2LTdjMzUtMTRkNy00NjZjYjNmMDkxMDMiLCJtZXRhU2l0ZUlkIjoiMDg4MDljZDctNDhiMy00MmZiLWE0NzAtNTI0YTBkMWZiM2RkIiwic2lnbkRhdGUiOiIyMDIxLTAyLTE0VDIxOjQ5OjAzLjk3NVoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjIzMTRiZmVjLWQ4NjYtNDYyNC1hNzU5LTg2MWNiMGQ5MDc2ZSIsImJpVG9rZW4iOiI1Y2NjMzMxNy01OGJiLTA2NjUtMDU1OS1kMmMwZDUxNzAwZjEiLCJzaXRlT3duZXJJZCI6ImM2NDc1ZmVhLTllNTEtNGE2MS04NjM2LTkyNjVmNDM4MjcwMyJ9&currency=GBP&currentCurrency=GBP&vsi=908a90f0-af79-41da-9590-29612c72b3ca&commonConfig=%7B%22brand%22%3A%22wix%22%2C%22bsi%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C3%22%2C%22BSI%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C3%22%7D",
            "https://social-blog.wix.com/custom-feed-widget?pageId=ejf88&compId=comp-kbwnckqx&viewerCompId=comp-kbwnckqx&siteRevision=2588&viewMode=site&deviceType=desktop&locale=en&tz=America%2FNew_York&width=920&height=3296&instance=ui6twEcmgE2Seo_QrA3iefKVQB0OvBzDMyJNUCCajnU.eyJpbnN0YW5jZUlkIjoiNTQ0Y2FmYzAtMTAwOC00NDllLWExMjktODA4YWQ4MDhiMzJjIiwiYXBwRGVmSWQiOiIxNGJjZGVkNy0wMDY2LTdjMzUtMTRkNy00NjZjYjNmMDkxMDMiLCJtZXRhU2l0ZUlkIjoiMDg4MDljZDctNDhiMy00MmZiLWE0NzAtNTI0YTBkMWZiM2RkIiwic2lnbkRhdGUiOiIyMDIxLTAyLTE0VDIxOjQ5OjAzLjk3NVoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjIzMTRiZmVjLWQ4NjYtNDYyNC1hNzU5LTg2MWNiMGQ5MDc2ZSIsImJpVG9rZW4iOiI1Y2NjMzMxNy01OGJiLTA2NjUtMDU1OS1kMmMwZDUxNzAwZjEiLCJzaXRlT3duZXJJZCI6ImM2NDc1ZmVhLTllNTEtNGE2MS04NjM2LTkyNjVmNDM4MjcwMyJ9&currency=GBP&currentCurrency=GBP&vsi=908a90f0-af79-41da-9590-29612c72b3ca&commonConfig=%7B%22brand%22%3A%22wix%22%2C%22bsi%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C10%22%2C%22BSI%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C10%22%7D",
            "https://social-blog.wix.com/custom-feed-widget?pageId=motbs&compId=comp-kbwo1f6o&viewerCompId=comp-kbwo1f6o&siteRevision=2588&viewMode=site&deviceType=desktop&locale=en&tz=America%2FNew_York&width=920&height=658&instance=ui6twEcmgE2Seo_QrA3iefKVQB0OvBzDMyJNUCCajnU.eyJpbnN0YW5jZUlkIjoiNTQ0Y2FmYzAtMTAwOC00NDllLWExMjktODA4YWQ4MDhiMzJjIiwiYXBwRGVmSWQiOiIxNGJjZGVkNy0wMDY2LTdjMzUtMTRkNy00NjZjYjNmMDkxMDMiLCJtZXRhU2l0ZUlkIjoiMDg4MDljZDctNDhiMy00MmZiLWE0NzAtNTI0YTBkMWZiM2RkIiwic2lnbkRhdGUiOiIyMDIxLTAyLTE0VDIxOjQ5OjAzLjk3NVoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjIzMTRiZmVjLWQ4NjYtNDYyNC1hNzU5LTg2MWNiMGQ5MDc2ZSIsImJpVG9rZW4iOiI1Y2NjMzMxNy01OGJiLTA2NjUtMDU1OS1kMmMwZDUxNzAwZjEiLCJzaXRlT3duZXJJZCI6ImM2NDc1ZmVhLTllNTEtNGE2MS04NjM2LTkyNjVmNDM4MjcwMyJ9&currency=GBP&currentCurrency=GBP&vsi=908a90f0-af79-41da-9590-29612c72b3ca&commonConfig=%7B%22brand%22%3A%22wix%22%2C%22bsi%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C13%22%2C%22BSI%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C13%22%7D",
            "https://social-blog.wix.com/custom-feed-widget?pageId=g74dm&compId=comp-kbwo1zpx&viewerCompId=comp-kbwo1zpx&siteRevision=2588&viewMode=site&deviceType=desktop&locale=en&tz=America%2FNew_York&width=920&height=3404&instance=ui6twEcmgE2Seo_QrA3iefKVQB0OvBzDMyJNUCCajnU.eyJpbnN0YW5jZUlkIjoiNTQ0Y2FmYzAtMTAwOC00NDllLWExMjktODA4YWQ4MDhiMzJjIiwiYXBwRGVmSWQiOiIxNGJjZGVkNy0wMDY2LTdjMzUtMTRkNy00NjZjYjNmMDkxMDMiLCJtZXRhU2l0ZUlkIjoiMDg4MDljZDctNDhiMy00MmZiLWE0NzAtNTI0YTBkMWZiM2RkIiwic2lnbkRhdGUiOiIyMDIxLTAyLTE0VDIxOjQ5OjAzLjk3NVoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjIzMTRiZmVjLWQ4NjYtNDYyNC1hNzU5LTg2MWNiMGQ5MDc2ZSIsImJpVG9rZW4iOiI1Y2NjMzMxNy01OGJiLTA2NjUtMDU1OS1kMmMwZDUxNzAwZjEiLCJzaXRlT3duZXJJZCI6ImM2NDc1ZmVhLTllNTEtNGE2MS04NjM2LTkyNjVmNDM4MjcwMyJ9&currency=GBP&currentCurrency=GBP&vsi=908a90f0-af79-41da-9590-29612c72b3ca&commonConfig=%7B%22brand%22%3A%22wix%22%2C%22bsi%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C15%22%2C%22BSI%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C15%22%7D",
            "https://social-blog.wix.com/custom-feed-widget?pageId=irlo9&compId=comp-kcazzhz0&viewerCompId=comp-kcazzhz0&siteRevision=2588&viewMode=site&deviceType=desktop&locale=en&tz=America%2FNew_York&width=920&height=290&instance=ui6twEcmgE2Seo_QrA3iefKVQB0OvBzDMyJNUCCajnU.eyJpbnN0YW5jZUlkIjoiNTQ0Y2FmYzAtMTAwOC00NDllLWExMjktODA4YWQ4MDhiMzJjIiwiYXBwRGVmSWQiOiIxNGJjZGVkNy0wMDY2LTdjMzUtMTRkNy00NjZjYjNmMDkxMDMiLCJtZXRhU2l0ZUlkIjoiMDg4MDljZDctNDhiMy00MmZiLWE0NzAtNTI0YTBkMWZiM2RkIiwic2lnbkRhdGUiOiIyMDIxLTAyLTE0VDIxOjQ5OjAzLjk3NVoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjIzMTRiZmVjLWQ4NjYtNDYyNC1hNzU5LTg2MWNiMGQ5MDc2ZSIsImJpVG9rZW4iOiI1Y2NjMzMxNy01OGJiLTA2NjUtMDU1OS1kMmMwZDUxNzAwZjEiLCJzaXRlT3duZXJJZCI6ImM2NDc1ZmVhLTllNTEtNGE2MS04NjM2LTkyNjVmNDM4MjcwMyJ9&currency=GBP&currentCurrency=GBP&vsi=908a90f0-af79-41da-9590-29612c72b3ca&commonConfig=%7B%22brand%22%3A%22wix%22%2C%22bsi%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C16%22%2C%22BSI%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C16%22%7D",
            "https://social-blog.wix.com/custom-feed-widget?pageId=impac&compId=comp-kbwo282j&viewerCompId=comp-kbwo282j&siteRevision=2588&viewMode=site&deviceType=desktop&locale=en&tz=America%2FNew_York&width=920&height=3262&instance=ui6twEcmgE2Seo_QrA3iefKVQB0OvBzDMyJNUCCajnU.eyJpbnN0YW5jZUlkIjoiNTQ0Y2FmYzAtMTAwOC00NDllLWExMjktODA4YWQ4MDhiMzJjIiwiYXBwRGVmSWQiOiIxNGJjZGVkNy0wMDY2LTdjMzUtMTRkNy00NjZjYjNmMDkxMDMiLCJtZXRhU2l0ZUlkIjoiMDg4MDljZDctNDhiMy00MmZiLWE0NzAtNTI0YTBkMWZiM2RkIiwic2lnbkRhdGUiOiIyMDIxLTAyLTE0VDIxOjQ5OjAzLjk3NVoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjIzMTRiZmVjLWQ4NjYtNDYyNC1hNzU5LTg2MWNiMGQ5MDc2ZSIsImJpVG9rZW4iOiI1Y2NjMzMxNy01OGJiLTA2NjUtMDU1OS1kMmMwZDUxNzAwZjEiLCJzaXRlT3duZXJJZCI6ImM2NDc1ZmVhLTllNTEtNGE2MS04NjM2LTkyNjVmNDM4MjcwMyJ9&currency=GBP&currentCurrency=GBP&vsi=908a90f0-af79-41da-9590-29612c72b3ca&commonConfig=%7B%22brand%22%3A%22wix%22%2C%22bsi%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C17%22%2C%22BSI%22%3A%2207af3657-02bd-4729-ba90-958bc7091995%7C17%22%7D"
            ]
folder_num = 1
for iframe_link in iframes:
    newpath = rf'file_outputs/folder{folder_num}'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    imagepath = rf'images/folder{folder_num}'
    if not os.path.exists(imagepath):
        os.makedirs(imagepath)

    page_url = iframe_link

    called_url = ureq(page_url)

    page_html = called_url.read()

    called_url.close()

    page_soup = soup(page_html, "html.parser")




    # This will find all of the links from the iframe html
    links = page_soup.findAll("a")
    link_href = []
    for item in range(len(links)):
        link_href.append(links[item].attrs['href'])
        

    link_href = list(dict.fromkeys(link_href))

    print(link_href)

        
    for individual_blog in link_href:


        page_url = individual_blog

        called_url = ureq(page_url)

        page_html = called_url.read()

        called_url.close()

        blog_soup = soup(page_html, "html.parser")

        # Find the title from the individual blog

        title = blog_soup.find("span", {"class": "blog-post-title-font"}).getText()
        
        f = open(f"file_outputs/folder{folder_num}/{title}.txt", "w+")
        f.write(title)
        f.close()
    

        #  Get all the text from the individual blog

        article = blog_soup.find("article")
        all_spans = article.findAll("span")
        all_href = article.findAll("a")
        all_images = article.findAll("img")


        #  Get all the text in the article
        f=open(f"file_outputs/folder{folder_num}/{title}.txt", "a+")
        for text in range(len(all_spans)):
            just_text = all_spans[text].getText()
    
            f.write(f"{just_text} \r\n")
        

        #  Get all the href in the article and the text to attach the link too.
        f.write("These are all the in text references. First is the word that was missing from the text and then the link. \n\r\n")
        for href in range(len(all_href)):
            just_href = all_href[href].attrs['href']
            href_text = all_href[href].getText()
            f.write(f"{href_text} \n")
            f.write(f"{just_href} \n\r\n")

        f.close()
        
      
        list_of_images_in_article = []
        for img in range(len(all_images)):
            just_image = all_images[img].attrs['data-pin-media']
            list_of_images_in_article.append(just_image)

        i = 1
        # Opening an image and downloading it.
        for img in list_of_images_in_article:
            img_number = f"images/folder{folder_num}/article-{title}-img{i}"
            resource = ureq(img)
            output = open(f"{img_number}.jpg","wb")
            output.write(resource.read())
            output.close()
            i = i + 1

    folder_num = folder_num + 1

end = time.time()
print("Time taken: " + str(end - start))
