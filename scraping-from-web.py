# First download *beautifulsoup4*, requests and *lxml* with pip3

from bs4 import BeautifulSoup
import requests
import time

print('Please type a skill you are not familiar with')
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}")

def find_jobs():
    html_text = requests.get('https://www.free-work.com/en-gb/tech-it/jobs?query=Python').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_='px-4 pb-4 flex flex-col h-full')
    for index, job in enumerate(jobs):
        company_name = job.find('div', class_='text-base font-medium truncate w-full').text.replace(' ', '')
        if 'ICResources' not in company_name:
            continue
        skills = job.find('div', class_='line-clamp-3 mb-4').text
        published_date = job.find('div', class_='text-sm whitespace-nowrap').text
        salary = job.find('span', class_='flex-1').text
        location = job.find('span', class_='block flex-1 truncate').text
        more_info = job.h3.a['href']

        if unfamiliar_skill not in skills:
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"Company Name: {company_name.strip()}\n")
                f.write(f"Salary: {salary.strip()}\n")
                f.write(f"Published Date: {published_date.strip()}\n")
                f.write(f"Required Skills: {skills.strip()}\n")
                f.write(f"Location: {location.strip()}\n")
                f.write(f"More info: {more_info}\n")
            print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)