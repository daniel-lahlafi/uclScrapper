import requests
from bs4 import BeautifulSoup
import lxml

def scrapeJobShop():
    jobsList = []
    page = 0

    while True:
        resp = requests.get('http://studentsunionucl.org/jobshop?page=' + str(page)).text
        soup = BeautifulSoup(resp, 'lxml') #Used for parsing the website

        jobCards = soup.findAll('a', attrs={'class': 'clubs events jobshop-card'})

        # Stop when you run out of jobs
        if len(jobCards) == 0:
            break

        for job in jobCards:
            # Get array of the information about the job
            contentArray = job.findAll('span')

            # Skip a job if it is missing information
            if len(contentArray) < 4:
                continue

            # Extract the content from the job html code
            for x in range(len(contentArray)):
                contentArray[x] = contentArray[x].text.replace('\n', '').strip()

            # Perform formating on the wage of the job
            contentArray[3] = " ".join(contentArray[3].split())
          

            # jobCards[0]['href'] gives the link to the Job
            # contentArray[0] gives the name of the job
            # contentArray[1] gives the name of the company
            # contentArray[3] gives the pay

            jobsList.append([job['href'], contentArray[0], contentArray[1], contentArray[3]])

        page += 1
    return jobsList

def scrapeEvents():
    eventsList = []
    page = 0

    while True:
        resp = requests.get('http://studentsunionucl.org/whats-on/list?page=' + str(page)).text
        soup = BeautifulSoup(resp, 'lxml') #Used for parsing the website

        # A list of the HTML of the events cards
        eventCards = soup.findAll('a', attrs={'class': 'clubs events'})

        # Stop when you run out of events
        if len(eventCards) == 0:
            break

        for event in eventCards:
            # Get array of information about the event
            contentArray = event.findAll('p')

            # Ignore the event if information is missing 
            if len(contentArray) < 4:
                continue

            #Extract the content from the job html code
            for x in range(len(contentArray)):
                contentArray[x] = contentArray[x].text.replace('\n', '').strip()
            
            # event['href'] gives the link to the Job
            # contentArray[0] gives the location
            # contentArray[1] gives the date
            # contentArray[2] gives the organiser
            # contentArray[3] gives the name of the event 

            eventsList.append([event['href'], contentArray[0], contentArray[1], contentArray[2], contentArray[3]])
        
        page += 1
    return eventsList
