import sys
print(sys.path)

from mmpose.apis import (init_pose_model, inference_bottom_up_pose_model, vis_pose_result)
path_to_general_folder = '/home/maria/Escritorio/TFM/TFM_MariaUrbiola/'
path_to_image_folder = path_to_general_folder + 'mmpose_photos/'

config_file = path_to_general_folder + 'mmpose/associative_embedding_hrnet_w32_coco_512x512.py'
checkpoint_file = path_to_general_folder + 'mmpose/hrnet_w32_coco_512x512-bcb8c247_20200816.pth'
pose_model = init_pose_model(config_file, checkpoint_file, device='cpu')  # or device='cuda:0'

image_name = path_to_image_folder + 'persons.jpg'
# test a single image
pose_results, _ = inference_bottom_up_pose_model(pose_model, image_name)

# show the results
vis_pose_result(pose_model, image_name, pose_results, out_file= path_to_image_folder+'vis_persons.jpg')