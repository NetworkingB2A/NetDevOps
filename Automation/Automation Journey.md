how it started?
Two incidents come to mind
- There was a dangerous fire at a oil refinery company we had to evacuate our offices in that area. At the time we really only had one DHCP server that was serving out ip addresses for the business unit that i was working in. We were freaking out that we wouldnt be able to hand out ip address to all of our users the next day. We came with a plan to create a new dhcp server, then we had to deploy this new dhcp servers to all the routers in out area. talking about 200 routers. What did we do in the before times, we got 4 or 5 people together. we got a list of all the routers and each one of us started to hand bomb in the config.
- I was working on a project to update about 260 routers, the task included gather information about the current routers, configure a brand new router, create a configuration for an existing router, create change details for every pair of routers and a have a uniform deployment guide.
  - at first the way I was told to deploy this was take my base script, put the script into one tab. then take use a find and replace to find a variable and replace the with data. This worked when i did the first 15 sites, but thinking that I would have to do this over a hundred more times, and the amount of errors I had in the just the first 15 we very defeating feeling.
  - This is where my first bit of automation came into play. I wrote a terrible script that would log into each device and gather the info I needed from it. The script would log into a device, run the show commands and output it into a text file. I would then copy paste all the data I needed out of that text file.
  - I wrote a jinja script that would take my data and create a config file. The config files were the actual configuration I would apply to the devices.
  - That was really as far as I took that script.

After I used automation for those tasks, I ended up not using automation for a while.


Some mistakes I made
- I would spend all of my time learning about automation or about scripting but I would not sit down and actually write some code.
- I battled back and forth learning different platforms or DSL that i would not become proficient with any of them.
  - example here was i would try and learn python for a few weeks, then move over to ansible for a couple months, but I never constantly sat down and fully learned the two.
- Sometimes I worried too much about the cost benefit of doing some automation. that I ended up taking the shortcut and doing a task the manual way.
  - Example maybe I needed to go and check 20 devices to see if they had a certain config. Instead of writing some automation to check devices for that config, I would just manually go and check the devices.
- I spend too much time setting up environments instead of spending the time writing the code.
- I let others dictate my training instead of just sticking what I wanted to learn.
- Sometime I would stop learning something mid training because I would not understand the code they wrote. I would then spend hours going down rabbit holes to understand the code that someone else had written.
- I would get mad at myself because I code was not written well, I would try and make it better, but then my code would brake I couldnt get it working back how i wanted it so I would give up.
- I tried to write the code perfectly the first time and have it written for an enterprise level.


Some wins for me
- Writing the first bit of automation that helped me to create 
  - There was a small bit of a loss here as well. I wrote the initial version of the Jinja template, but someone who was better at coding than I took the code and rewrote it. They changed up some critical features to me, example( forcing me to try and create yaml file per device I wanted to configure, where I wanted to create a single CSV that housed the data for all of the devices. Looking back I think both of us where right.)  one of the main issues was the code he wrote was better than what i was capable at the time. I asked for his help to explain the code better to me, but communication was not our strong suits, so when he would explain, I did not understand.
- Creating Ansible playbook that can help with lifecycle of equipment.
  - it would create the config of a new device based on the yaml file you created.
  - It would also reach out to a device and build a yaml file based on was on that device. then you can go and look over that yaml file and see if its correct.
  - This one was a huge win, in the fact that as we change our templates, you dont have to update your version of the template that you saved to your computer.
- I haven't contibuited to much open source projects, but I have found two bugs in their software. I am not saying this to say how great I am. I am saying this because these two case I really felt that accomplished something that i didn't think i could. These made my feel super good about myself after having so many what i felt like to be failures in the past.
  - one was with a nautobot plug in,
  - other was a cisco dnac ansible plugin.
- Recent one was after failing many many many times, I wrote my first test case for check to see if any image is on a device.


Some important learnings for me
- Automation is not easy
- Software development is not easy
- trying to automate a end to end workflow is impossible if you dont break it down.
  - Patching a device start to finish is too much work.
  - You must break this workflow down to tasks. Understand there are technical tasks and that there are business tasks.
    - activating an image on a device is both a technical task and a business task.
    - The business might tell you when to active the image, but do the checks to see if the image is on the device, if the image passes a MD5 hash, what is the state pre activate and post activation.
- Plan, deploy small features and be ready to scrape or completely change something you are working on.
- Don't spend too much time on low hanging fruit. low hanging fruit is important, but in my experience spending all the time on the low hanging fruit, I feel like I have created a lot of script that only i can run.
- Document as you go. when writing code continue to write down how to use the code, why you did things a certain way.
- Don't watch code habits that only noobs do, type of videos. I think that is one thing that hurt me in the long run.
- 