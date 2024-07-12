#This script is run specifically to scrape the info from the website

#download library
import kaggle # type: ignore

#will automatically look for the file in '.kaggle' directory
#created my own API beforehand
kaggle.api.authenticate() 

#downloads the data
kaggle.api.dataset_download_files('stefanzivanov/olympic-games-2021-medals', path='.', unzip=True)