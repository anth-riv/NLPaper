import requests

url = 'http://127.0.0.1:5000/summarize'

data = {
    "text": "The Environment In our modern world, there are many factors that place the wellbeing of the planet in jeopardy. While some people have the opinion that environmental problems are just a natural occurrence, others believe that human beings have a huge impact on the environment. Regardless of your viewpoint, take into consideration the following factors that place our environment as well as the planet Earth in danger. Global warming or climate change is a major contributing factor to environmental damage. Because of global warming, we have seen an increase in melting ice caps, a rise in sea levels, and the formation of new weather patterns. These weather patterns have caused stronger storms, droughts, and flooding in places that they formerly did not occur. Air pollution is primarily caused as a result of excessive and unregulated emissions of carbon dioxide into the air. Pollutants mostly emerge from the burning of fossil fuels in addition to chemicals, toxic substances, and improper waste disposal. Air pollutants are absorbed into the atmosphere, and they can cause smog, a combination of smoke and fog, in valleys as well as produce acidic precipitation in areas far away from the pollution source. In many areas, people and local governments do not sustainably use their natural resources. Mining for natural gases, deforestation, and even improper use of water resources can have tremendous effects on the environment. While these strategies often attempt to boost local economies, their effects can lead to oil spills, interrupted animal habitats, and droughts. Ultimately, the effects of the modern world on the environment can lead to many problems. Human beings need to consider the repercussions of their actions, trying to reduce, reuse, and recycle materials while establishing environmentally sustainable habits. If measures are not taken to protect the environment, we can potentially witness the extinction of more endangered species, worldwide pollution, and a completely uninhabitable planet."
}

response = requests.post(url, json=data)

print(response.json())
