# automatic-segmentation-Software--integrating-STCN-U-Net-series-and-DPU-Net
this is a small PyQt5 software that can achieve automatic segmentation of image sequences
  I am terribly sorry that these are all the files that aren't "TOO BIG"
  you can find the models that are supposed to be integrated via my other repositories:
  1. see DPU, U-Net, WPU-Net at: https://github.com/Karl-7/DPU-Net_Double-Propagation-for-segmentation-and-tracking-of-material-microscopic-image-sequences
  2. see my formalized(generalized) STCN at: https://github.com/Karl-7/STCN_for_software_integration
  and please prepare your own dataset, as mine is too big to upload.
HOW TO USE :
  1. prepare your own dataset with the following structure :
  <img width="129" alt="image" src="https://github.com/Karl-7/automatic-segmentation-Software--integrating-STCN-U-Net-series-and-DPU-Net/assets/142679657/22be4e46-a6bc-4b4f-b5d3-e3a5793458b7">
  
  2. download the 2 kinds of models mentioned above, and put them in the same folder with the files in this repository. like:
  <img width="529" alt="image" src="https://github.com/Karl-7/automatic-segmentation-Software--integrating-STCN-U-Net-series-and-DPU-Net/assets/142679657/1823bbaa-d648-4511-8a59-0cec4f6c78bb">
  
  3. start the main_ui.py, run it and so you can see the following outcomes:
     pic 1. main UI
     <img width="500" alt="image" src="https://github.com/Karl-7/automatic-segmentation-Software--integrating-STCN-U-Net-series-and-DPU-Net/assets/142679657/6050d2e5-ae7e-4f24-be94-fb98890d186e">

     pic 2. after you entered your dataset address, the UI updates
     <img width="470" alt="image" src="https://github.com/Karl-7/automatic-segmentation-Software--integrating-STCN-U-Net-series-and-DPU-Net/assets/142679657/ca4ea79f-99c6-4a25-95e3-1703e13efeac">

     pic 3. during training/testing
     <img width="470" alt="image" src="https://github.com/Karl-7/automatic-segmentation-Software--integrating-STCN-U-Net-series-and-DPU-Net/assets/142679657/902e975d-f5cb-40b6-b993-bca6df472338">

     pic 4. after evaluating, the UI updates
     <img width="455" alt="image" src="https://github.com/Karl-7/automatic-segmentation-Software--integrating-STCN-U-Net-series-and-DPU-Net/assets/142679657/423552bb-ad7e-4f27-b6f5-6eb73d43fd14">
