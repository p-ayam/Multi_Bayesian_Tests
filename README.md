# Multi_Bayesian_Tests


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/p-ayam/Multi_Bayesian_Tests/HEAD)

## An Online Calculator for Crunching My Test Numbers


<p align="center">
<img src="https://github.com/p-ayam/images/blob/main/title_Bayes.jpg" alt="alt text" width="400" height="whatever">
</p>

Last year, a totally asymptomatic Covid case knocked on my door and made me go through some unexpected isolation time. Thanks to the magic of the vaccines, though, everything turned out to be milder than my mildest cold. On top of that, I was super lucky to be able to spot the infection early on before spreading it further. In the race for maintaining the virus, time was on my side because of another technological marvel: rapid lateral flow tests (LFTs). 

LFTs are awesome! They are easy to use, fast, and affordable. Already, that makes them 3-0 ahead of the PCR team in this race ;-) This personal encounter with Covid, and my luck factor with LFTs, somehow woke up my "dig-down-the-rabbit-hole spirits" and convinced me to consult Dr. Google more about LFTs. Here, I thought I will share a brief version of my Q&A sessions with Dr. Google and showcase an online calculator that I made for checking how likely one has Covid, given the test results.

Before continuing, let me clarify that I am a total outsider to the field of virology and public health and I only wanna share my own understanding of the testing here. But I am fully open to learn, correct and revise :) With that in mind, let's go through this Q&A list:

#### What do LFTs do? 

They detect whether you are “shedding SARS-CoV-2 antigens” or not. ([link](https://www.dovepress.com/getfile.php?fileID=74968))

#### Why is that important? 

Because it can tell you if you are infectious with Covid or not! PCR tests, on the other hand, detect “genetic material left behind for a long period when the individual is no longer infectious”. ([link](https://www.dovepress.com/getfile.php?fileID=74968)). This means PCR can detect small traces of the virus even well beyond beyond the patient's infectiousness phase.

Wait! I thought if I have the virus, that means I am infectious, doesn't it?

It depends! Check out this graph by [Michael Mina](https://time.com/5912705/covid-19-stop-spread-christmas/):


#### Ok, ok, LFTs are cool and everything but at the end of the day, they are not so accurate. Right? 

Not necessarily! The values one reads about the sensitivity of LFTs are adjusted to the PCR results. If your goal is to detect the RNA leftovers of the virus with LFTs, then you will get a low sensitivity. But if your goal is to screen the infectiousness (public-health relevant) then LFTs provide a sensitivity well above 80%.([link](https://www.dovepress.com/getfile.php?fileID=74968)) 

In another insightful [data representation](https://twitter.com/michaelmina_lab/status/1438032854907301893/photo/1), [Michael Mina, MD, PhD](https://www.linkedin.com/in/michael-mina-md-phd-711918113?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABxvJv0BijhAYYDj5gB9hgkYAhRbpKsl7Jw&lipi=urn%3Ali%3Apage%3Ad_flagship3_publishing_post_edit%3BDic0mivzSFCIUZU6ZGsRsA%3D%3D) estimates the sensitivity of the LFT in detecting the infectious viral loads to be about 97%, with a specificity of 99.9%. His estimation is based on the data in [this](https://www.thelancet.com/journals/eclinm/article/PIIS2589-5370(21)00204-2/fulltext) paper.

#### But what does all this mean for me as an individual? 

It means frequent testing can increase your chances of capturing your potential infectiousness before you pass on the transmissible virus. Let’s go through two examples:

1. Imagine you live in a city with a 7-day incidence of 300 Covid cases per 100’000 inhabitants. One morning, you test yourself with LFT and you get a negative result. What does that mean? If you consider a test sensitivity of 80% and a specificity of 98%, your chances of actually being infectious (despite the negative result) is 0.06 %.

2. On the second day, you test yourself again with LFT and this time your result is positive! How bad of news is that? Given the same testing conditions, your probability of actually being infectious given that you have been tested positive is about 11 %. That is not a very compelling number, is it? 
Lucky enough, one can improve on this probability result by repeating the test. LFT’s speed, affordability and lack of side effects allow for <ins>2-3 repeated tests in less than an hour, with a cost below €10</ins>. 

Let’s do that: If you run another test and get tested positive again, your probability of being infectious will now rise to 83%. A third positive test result will make it pretty clear what is going on! You are infectious with a probability of 99% based on LFT. Ideally, one can run the tests with different brands for keeping the results as independent as possible.

<p align="center">
<img src="https://github.com/p-ayam/images/blob/main/App_Bayes.jpg" alt="alt text" width="500" height="whatever">
</p>

If you want to check your own probability numbers more closely, you can look up [this](https://bayesian-tests.herokuapp.com/) dashboard that I made based on [repeated Bayesian tests](https://towardsdatascience.com/multiple-bayesian-tests-in-row-2e4ad8fb5055), using [dash](https://plotly.com/dash/).

#### Check your own numbers here:
[https://bayesian-tests.herokuapp.com/](https://bayesian-tests.herokuapp.com/)

One final comment: The points I shared here are mainly from the time before the emergence of the Omicron variant. I'm curious if they could still be applied to Omicron..
