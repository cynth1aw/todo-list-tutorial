class todo:
    id: int
    title: str
    description: str

    def __init__(self, id: int, title: str, description: str):
        self.id = id
        self.title = title
        self.description = description

# def gen():
#     i = 0

#     while True:
#         time.sleep(5)
#         images = get_all_images()
#         image_name = images[i]
#         im = open('images/' + image_name, 'rb').read()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + im + b'\r\n')
#         i += 1
#         if i >= len(images):
#             i = 0


# def get_all_images():
#     image_folder = 'images'
#     images = [img for img in os.listdir(image_folder)
#               if img.endswith(".jpg") or
#               img.endswith(".jpeg") or
#               img.endswith("png")]
#     return images