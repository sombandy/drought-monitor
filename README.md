## ChatGPT written code to create drought monitoring video

Used publicly available ChatGPT https://chat.openai.com/chat and the following prompts to generate the code

## prompt1

```Write a python code to output a list of URLs in a file where each URL is in the form https://droughtmonitor.unl.edu/data/png/<date>/<date>_usdm.png where <date> is in the form YYYYMMDD ranges from 20000104 to 20230314 incremented by 7 days```


The prompt is shown in the [screenshot prompt1](prompt1.png). The output is captured in the file [generate_urls.py](generate_urls.py)

There are state or region specific drought map images available in the site https://droughtmonitor.unl.edu/maps/maparchive.aspx. For example, to get the drought maps of california use the URL pattern `https://droughtmonitor.unl.edu/data/png/<date>/<date>_ca_trd.png`

## prompt2
```Write a python code which takes a file named urls.txt containing list of image urls as input and generates a mp4 video with those images. Give 0.1 sec delay between downloading subsequent images ```

The prompt is shown in the [screenshot prompt2](prompt2.png). The output is captured in the file [create_video.py](create_video.py)

It missed importing numpy which I had to manually add. I also added the print statement to monitor the progress.