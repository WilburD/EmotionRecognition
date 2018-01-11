# EmotionRecognition

This repository contains demo and files in order to easily build and run an Emotion Recognition classifier. This model was trained using three popular datasets: **CK+** [1], **Bosphorus** [2] and **RafD** [3]. Training procedure is not supplied, but I can do it for sure if it is required. 

### Notebook
 - demo.ipynb

### Use: 
 - ./demo.py

### Requirements:
 - [caffe](https://github.com/BVLC/caffe)
 - opencv
 - *caffemodel weights* can be downloaded [here](https://drive.google.com/open?id=0B5SM4aR218blbnhCdDQ3ajYydFE)

---
## Demo is tested on these images:

![](/imgs/1.png)
![](/imgs/2.png)
![](/imgs/3.png)
![](/imgs/4.png)
![](/imgs/5.png)
![](/imgs/5.jpg)
![](/imgs/6.png)


---
**[1]** Lucey, P., Cohn, J. F., Kanade, T., Saragih, J., Ambadar, Z., & Matthews, I. (2010, June). The extended cohn-kanade dataset (ck+): A complete dataset for action unit and emotion-specified expression. In Computer Vision and Pattern Recognition Workshops (CVPRW), 2010 IEEE Computer Society Conference on (pp. 94-101). IEEE.

**[2]** Savran, A., Alyüz, N., Dibeklioğlu, H., Çeliktutan, O., Gökberk, B., Sankur, B., & Akarun, L. (2008). Bosphorus database for 3D face analysis. Biometrics and identity management, 47-56.

**[3]** Langner, O., Dotsch, R., Bijlstra, G., Wigboldus, D. H., Hawk, S. T., & Van Knippenberg, A. D. (2010). Presentation and validation of the Radboud Faces Database. Cognition and emotion, 24(8), 1377-1388.
