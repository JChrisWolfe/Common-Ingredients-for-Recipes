{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Common Pantry Ingredents for Well-balanced or Healthy Meals\n",
    "\n",
    "## Author: James Christopher Wolfe\n",
    "\n",
    "This Python Notebook helps determine common ingredents for your pantry when making healthy or well-balanced meals by referencing information from the Food Network website."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Grab essential Modules for the Beautiful Soup 4 module\n",
    "We are going to need to import the essential modules for Web Services and using [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/) module."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import urllib.request, urllib.parse, urllib.error # Get modules on HTTP request on handling, parsing, and errors.\n",
    "from bs4 import BeautifulSoup\n",
    "import ssl"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Ignoring any SSL errors\n",
    "To prevent any Secure Socket Layer errors as we browse the Food Network site we'll need to write code that ignores the SSL expires or any other errors. This is just in case the Food Network forgets to update their SSL certificate or something else that went wrong."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "ctx = ssl.create_default_context()\n",
    "ctx.check_hostname = False\n",
    "ctx.verify_mode = ssl.CERT_NONE"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### We need to grab the URL\n",
    "We need the Food Network URL on [Basic Pantry 101](https://www.foodnetwork.com/recipes/articles/basic-pantry-101)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://www.foodnetwork.com/recipes/articles/basic-pantry-101\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Read HTTP request and pass our information into the Beautiful Soup Object.\n",
    "We'll create a variable \"html\" that stores the HTML source code from the HTTP request (urllib.request) as a 'bytes' object. Afterwards create variable \"soup\" which acts as an instance of the BeautifulSoup class, pass the 'html' and 'html.parser' as parameters.\n",
    "\n",
    "*Note:* 'html.parser' or called the [HTML parser](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser) is in the standard Python 3 library."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = urllib.request.urlopen(url) \n",
    "# type(html) # Type returns \"http.client.HTTPResponse\"\n",
    "html = urllib.request.urlopen(url, context=ctx).read() # Need \"context=ctx\" to ignore SSL\n",
    "# type(html) $ returns \"bytes\" which is a type of Object in Python, try \"dir(html)\"\n",
    "\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Retrieve the Section Tag and break it down\n",
    "**References:** \n",
    "(1) [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)\n",
    "(2) [Python Nerds Beautiful Soup](https://youtu.be/d4no8cNmCDE)\n",
    "(3) Lots of StackOverFlow and Google Searching\n",
    "\n",
    "In the [Basic Pantry 101](https://www.foodnetwork.com/recipes/articles/basic-pantry-101) page we need to get the `<section>` tag that has a `class=\"o-CustomRTE\"`. It contains the list of types of pantry items and the specific ingredents. It contains `<p>` tags that shows the different types of pantry items and the `<ul>` tags that show a list of all specific ingredents of those types in the `<p>` tags.\n",
    "    \n",
    "We are just going to print every `<p>` tag based in the `<section>` tag and every `<ul>` tag after each `<p>` tags.\n",
    "    \n",
    "We'll also just going to print the Information in a nice format to see what we're doing."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "~ Oils, Vinegars and Condiments\n",
      "\n",
      "-- Oils: canola oil, extra-virgin olive oil, toasted sesame\n",
      "-- Vinegars: balsamic, distilled white, red wine, rice\n",
      "-- Ketchup\n",
      "-- Mayonnaise\n",
      "-- Dijon mustard\n",
      "-- Soy sauce\n",
      "-- Chili paste\n",
      "-- Hot sauce\n",
      "-- Worcestershire\n",
      " \n",
      "====================================\n",
      "~ Seasonings\n",
      "\n",
      "-- Kosher salt\n",
      "\n",
      "-- Black peppercorns\n",
      "\n",
      "-- Dried herbs and spices: bay leaves, cayenne pepper, crushed red pepper, cumin, ground coriander, oregano, paprika, rosemary, thyme leaves, cinnamon, cloves, allspice, ginger, nutmeg\n",
      "\n",
      "-- Spice blends: chili powder, curry powder, Italian seasoning\n",
      "\n",
      "-- Vanilla extract\n",
      "====================================\n",
      "~ \n",
      "Canned Goods and Bottled Items\n",
      "\n",
      "-- Canned beans: black, cannellini, chickpeas, kidney\n",
      "\n",
      "-- Capers\n",
      "\n",
      "-- Olives\n",
      "\n",
      "-- Peanut butter\n",
      "\n",
      "-- Preserves or jelly\n",
      "\n",
      "-- Low-sodium stock or broth\n",
      "\n",
      "-- Canned tomatoes\n",
      "\n",
      "-- Tomatoes, canned and paste\n",
      "\n",
      "-- Salsa\n",
      "\n",
      "-- Tuna fish\n",
      "\n",
      "\n",
      "====================================\n",
      "~ Grains and Legumes\n",
      "\n",
      "-- Breadcrumbs: regular, panko\n",
      "\n",
      "-- Couscous\n",
      "\n",
      "-- Dried lentils\n",
      "\n",
      "-- Pasta: regular, whole wheat\n",
      "\n",
      "-- Rice\n",
      "\n",
      "-- Rolled oats\n",
      "\n",
      "-- One other dried grain: try barley, millet, quinoa or wheatberries\n",
      "\n",
      "\n",
      "====================================\n",
      "~ Baking Products\n",
      "\n",
      "-- Baking powder\n",
      "\n",
      "-- Baking soda\n",
      "\n",
      "-- Brown sugar\n",
      "\n",
      "-- Cornstarch\n",
      "\n",
      "-- All-purpose flour\n",
      "\n",
      "-- Granulated sugar\n",
      "\n",
      "-- Honey\n",
      "\n",
      "\n",
      "====================================\n",
      "~ Refrigerator Basics\n",
      "\n",
      "-- Butter\n",
      "\n",
      "-- Cheese: sharp cheddar, feta, Parmesan, mozzarella\n",
      "\n",
      "-- Large eggs\n",
      "\n",
      "-- Milk\n",
      "\n",
      "-- Plain yogurt\n",
      "\n",
      "-- Corn tortillas\n",
      " \n",
      "====================================\n",
      "~ Freezer Basics\n",
      "\n",
      "-- Frozen fruit: blackberries, blueberries, peaches, strawberries\n",
      "\n",
      "-- Frozen vegetables: broccoli, bell pepper and onion mix, corn, edamame, peas, spinach\n",
      "\n",
      "\n",
      "====================================\n",
      "~ Storage Produce\n",
      "-- Garlic\n",
      "\n",
      "-- Onions (red, yellow)\n",
      "\n",
      "-- Potatoes\n",
      "\n",
      "-- Dried fruit: raisins, apples, apricots\n",
      "\n",
      "-- Nuts or seeds: almonds, peanuts, sunflower\n",
      "\n",
      "====================================\n"
     ]
    }
   ],
   "source": [
    "article_list = soup.find(\"section\", class_ = \"o-CustomRTE\")\n",
    "\n",
    "for items in article_list.find_all('p'):\n",
    "    print(\"~\", items.text)\n",
    "    for li in items.find_next_sibling('ul').find_all('li'):\n",
    "        print(\"--\", li.text)\n",
    "    print(\"====================================\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
