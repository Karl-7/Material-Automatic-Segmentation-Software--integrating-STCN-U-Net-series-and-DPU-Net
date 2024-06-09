import sys
import os
import torch
sys.path.append('/root/data/videoanno/STCN_main/TRAIN_SETTINGS.py')
sys.path.append('/root/data/videoanno/WPU-Net-master/TRAIN_PARAS.py')
sys.path.append('/root/data/videoanno/WPU-Net-master/TRAIN_SETTINGS.py')
import STCN_main.TRAIN_SETTINGS
import WPU_Net_master.TRAIN_SETTINGS
def train_test_metric_start(dataset_address,model_choice,train_val_metric_state):
        # cwd =os.path.dirname(os.path.abspath(__file__))#'C:/......QT5_VOS_SLICER'  
        model=model_choice
        state=train_val_metric_state
        torch.cuda.empty_cache()
    
        if model=="STCN":
            model=STCN_main.TRAIN_SETTINGS.train_test(dataset_address)
            if state=="train":
                model.run_train()
            elif state=="test":
                model.run_test()
            elif state=="metric":
                model.confrontation()
        elif model=="U-Net":
            model=WPU_Net_master.TRAIN_SETTINGS.train_test(dataset_address,model)
            if state=="train":
                model.run_train()
            elif state=="test":
                model.run_test(model)
            elif state=="metric":
                model.confrontation()
        elif model=="WPU-Net":
            model=WPU_Net_master.TRAIN_SETTINGS.train_test(dataset_address,model)
            if state=="train":
                model.run_train()
            elif state=="test":
                model.run_test(model)
            elif state=="metric":
                model.confrontation()
        elif model=="DPU-Net":
            model=WPU_Net_master.TRAIN_SETTINGS.train_test(dataset_address,model)
            if state=="train":
                model.run_train()
            elif state=="test":
                model.run_test(model)
            elif state=="metric":
                model.confrontation()
                # Call the other function here
        else:
            import PyQt5.QtWidgets as QtWidgets
            QtWidgets.QMessageBox.information(None, "提示", "您没有选择模型！")
