import os
print('path', os.path.dirname(__file__))

from mmpose.apis import (init_pose_model, inference_bottom_up_pose_model, vis_pose_result)

def runImageFileDetection(file_path):
    
    #path_to_image_folder = os.path.dirname(__file__) + '/mmpose_photos/'

    config_file = os.path.dirname(__file__) + '/mmpose/associative_embedding_hrnet_w32_coco_512x512.py'
    checkpoint_file = os.path.dirname(__file__) + '/mmpose/hrnet_w32_coco_512x512-bcb8c247_20200816.pth'
    pose_model = init_pose_model(config_file, checkpoint_file, device='cpu')  # or device='cuda:0'

    #image_name = file_path + 'persons.jpg'
    # test a single image
    pose_results, _ = inference_bottom_up_pose_model(pose_model, file_path)

    # show the results
    vis_pose_result(pose_model, file_path, pose_results, out_file= os.path.dirname(__file__)+'/mmpose_photos/result2.jpg')    #cambiar esto porque lo guarda en home