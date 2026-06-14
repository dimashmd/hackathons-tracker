from bs4 import BeautifulSoup
import requests

# .text gets the text content of the webpage
mlh_html_text = requests.get("https://www.mlh.com/seasons/2026/events").text
soup = BeautifulSoup(mlh_html_text, "lxml")

sections = soup.find_all("section", class_ = "mb-16")

upcoming = sections[0]
upcoming_year = upcoming.find("h3", class_ = "text-xl font-semibold text-gray-600 mb-6").text
past = sections[1]
past_years = [year.text for year in past.find_all("h3", class_ = "text-xl font-semibold text-gray-600 mb-6")]

# finds all the event cards on the page
events = upcoming.find_all("a", class_="block no-underline hover:no-underline group")

# finds first event card on the page
event = upcoming.find("a", class_="block no-underline hover:no-underline group")
# or: first_event_card = events[0]

# finds the event name in the first event card
name = event.find("h4", class_ = "font-bold transition-colors duration-200 mb-0.5 line-clamp-2 text-black group-hover:text-blue-500 group-has-[.info-row-link:hover]:text-black text-xl md:text-2xl lg:text-2xl h-[3.5rem] md:h-[4.2rem] lg:h-[4.2rem]").text

logistics = event.find_all("span", class_ = "text-sm truncate")

link = event.get("href")

dates = logistics[0].text

location = logistics[1].text

banner = event.find("img", class_ = "w-full h-full group-hover:scale-105 group-has-[.info-row-link:hover]:scale-100 transition-transform duration-300 object-cover object-top").get("src")

logo = event.find("img", class_ = "w-full h-full object-cover").get("src")

# tags = event.find("span", class_ = "inline-flex items-center justify-center font-semibold uppercase tracking-wide border border-navy-100/20 h-7 px-3 text-xs bg-green-100 text-gray-900 rounded-full").text

print(f'''
Upcoming Year: {upcoming_year}
Event Name: {name}
Event Dates: {dates}
Event Location: {location}
Event Image URL: {banner}
Event Logo URL: {logo}
Event Link: {link} 
Past Years: {past_years}
''')