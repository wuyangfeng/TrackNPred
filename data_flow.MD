                ## DETECTION
                '''
                Input: 
                - .mp4 file

                Pre-processing:
                - dataDir, loaded from GUI, DEFAULT = "resources/data/TRAF"
                - dectect confidence score, DEFAULT = 0.8
                - nms(non-max-susspression), DEFAULT = 0.4
                - detection model (Yolo / Mask), DEFAULT = "YOLO"     
                - nfolders: number of folder in dataDir
                - detection loop orver all data_folders in dataDir
                - input_dir = dataDir + data_folder, e.g. "/resources/data/TRAF/TRAF13"
                - outputPath = input_dir + "det.txt", e.g. "/resources/data/TRAF/TRAF13/det.txt"
                - input_file = data_folder.mp4, e.g. TRAF13.mp4
                - frames: folder name (to store frames generated from mp4 file) loaded from GUI, DEFAULT = "frames"
                - outputFolder = input_dir + "detected_frames"

                Run detection: 
                - choose model (loaded from GUI), e.g. YOLO_detect 
                    self.model.YOLO_detect(input_dir, input_file, frames, "det.txt", "detectedFrames", conf, nms, args["cuda"], self)
                        execute model/Detection/Yolo/yolo_gpu.py
                            
                Output: 
                - raw frames generated from video
                - detected frames (with object bounding boxes)
                - det.txt file

                

                ## TRACKING
                
                Input: 
                det.txt
                
                Preprocessing:
                - dataDir, loaded from GUI, DEFAULT = "resources/data/TRAF"
                - nfolders: number of folder in dataDir

                Run Tracking:
                    self.model.tracking(dataDir, data_folder, thread=self)
                - densep_file_path = dataDir + data_folder + "densep.npy"
                - Generate Features: 
                    gen_feats(dataDir, data_folder, thread)
                - Pedestriants Tracking in dense Crowds using Front-RVO and Sparse Features
                    densepeds(dataDir, data_folder, display, thread)
                


                Output: 
                - detection_file = dataset + video folder + "/densep.npy"
                - output_file = dataset + videofolder + "/hypotheses.txt"
                - trackingFrames folder with tracked bounding boxes


                ## FORMATING
                


                ## PREDICTION
                Input: 
                hypotheses.txt

                Preprocessing:


                Run prediction:

                

                Output:
                formateted_hypo.txt
                TRAF13.npy


