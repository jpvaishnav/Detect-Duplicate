# Rrecommendation to remove duplicate images from the storage

### Method1
Use cv2.absdiff() function to compute the difference change
and remove the duplicate if it passes a certain threshold. (basic1.py)

### Method2
Get structural similarity index for comparing images. (basic2.py)

- Above methods won't work in case of alignment of same pictures 

### Method3
- Based on hamming distance (number of different bits in 2 numbers)
- hd > 10 => images are different
- Compute hash value of an image 
- delete images with similar hash value( main.py)

---

## Run
To detect duplicate
```html
python main.py --dataset dataset
```

To detect duplicate and remove them from dataset:
```html
python main.py --dataset dataset --remove 1
```

## Demo

![out](https://user-images.githubusercontent.com/46133803/85317498-179a1480-b4dc-11ea-880d-e4d16ed43bc5.gif)

## References
- https://www.pyimagesearch.com/2017/11/27/image-hashing-opencv-python/
- https://www.pyimagesearch.com/2020/04/20/detect-and-remove-duplicate-images-from-a-dataset-for-deep-learning/
