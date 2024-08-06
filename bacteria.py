from simple_image_download import simple_image_download as sim

my_downloader = sim.Downloader()

my_downloader.directory = 'my_dir/'
# Change File extension type
my_downloader.extensions = '.jpeg'
print(my_downloader.extensions)

my_downloader.download('Mycobacterium_tuberculosis', limit=50)
my_downloader.download('Staphylococcus_aureus', limit=50)