import requests
import bs4
import tkinter as tk

def get_html_data(url):
    data =requests.get(url)
    return data

def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_= "content-inner").findAll("div" ,  id="maincounter-wrap")
    all_data=" "

    for block in info_div:
        text = block.find("h1" , class_=None).get_text()
        count = block.find("span" , class_=None).get_text()
        all_data =all_data + text + " " + count + " \n "
        # print(all_data)

    return  "World Wide Corona Status \n "+all_data

get_covid_data()

root = tk.Tk()
root.geometry("900x700")
root.title("covid tracker")
f = ("poppins", 25 , "bold")

textfield=tk.Label(root, width=50)
textfield.pack()

mainlabel = tk.Label(root,  text=get_covid_data(), font=f)
mainlabel.pack()

root.mainloop()