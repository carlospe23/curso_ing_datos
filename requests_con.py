import requests
import bs4

response = requests.get('https://www.platzi.com')



# BEAUTIFUL SOUP

soup = bs4.BeautifulSoup(response.text, 'html.parser')

print(soup.title.text)
print(soup.select('meta[name=description]')[0]['content'])

courses_link = soup.select('.RecentCourses-item')
courses = [course.a['href'] for course in courses_link]

for i in courses:
    print(i)