from email.mime import image
from unicodedata import name


def get_courses():
    import requests
    from bs4 import BeautifulSoup
    url = 'https://yofreesamples.com/courses/free-discounted-udemy-courses-list/'
    agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    page = requests.get(url, headers=agent)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title_div = soup.find_all('div', class_='kt-inside-inner-col')
    total_course = len(title_div)
    figure = soup.find_all('figure', class_='wp-block-image')
    info = soup.find_all('p', class_='mb-10 mt-10')
    # print(info)
    courses = {}
    counter = 0
    images = []
    links = []
    titles = []
    while counter < total_course:
        
        for x in figure:
            a_tag = x.find('a')
            try :
                links.append(a_tag.get('href'))
                for img in a_tag.find_all('img'):
                    course_img = img.get('src')
                    if 'data' in course_img:
                        pass
                    else:
                        images.append(course_img)
                       


            except:
                pass
        
        for i in title_div:
            
            h4 = i.find('h4')
            try:
                for j in h4.find_all('a'):
                    # print(j.text)
                    # courses[j.get('href')] = j.text
                    titles.append(j.text)
            except:
                pass
            
        counter += 1
    
    
    
    
    
    for x in range(total_course):
        try:
            courses[titles[x]] = images[x], info[x].text ,links[x]
            print(courses.values()[images](titles[x]))
        except:
            pass
    
    return courses
    
    
    
    
    
    

#kt-layout-id_0975f2-c6 > div > div.wp-block-kadence-column.inner-column-2.kadence-column_99e5f9-78 > div