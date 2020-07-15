CUDA_VISIBLE_DEVICES=0 python video_inpaint.py --frame_dir ./demo/lady-running/frames \
--MASK_ROOT ./demo/lady-running/mask_bbox.png \
--img_size 448 896 --DFC --FlowNet2 --Propagation \
--PRETRAINED_MODEL_1 ./pretrained_models/resnet50_stage1.pth \
--PRETRAINED_MODEL_2 ./pretrained_models/DAVIS_model/davis_stage2.pth \
--PRETRAINED_MODEL_3 ./pretrained_models/DAVIS_model/davis_stage3.pth \
--MS --th_warp 3 --FIX_MASK
