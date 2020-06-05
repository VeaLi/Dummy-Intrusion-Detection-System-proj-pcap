# proj_pcap

Idea: classify traffic on anomaly/normal. If anomlay -> classify further
approach: generalization by machine learning

MainFlow:

	Dataset creation: labeled.pcap -> labeled.pcap_splitted by 1 second 
				       -> creating csv file with network packet description on each of splitted
				       -> feature extraction (for example - simple statistic calculation)
				       -> adding each record to TRAIN dataset
				       --> here should be evaluation (not performed)
	
	Model creation: using created labeled dataset:
				       -->choose model (not performed)
				       --> feature evaluation (basic evaluation perfomred) //conclusion not enough data -> delete stupid correlations
				       -> train logisticRegression anyway, perform crossvalidation.
				       -> save model as binary object using pickle or save weights of model if can be done (ex. lightgbm)
        Assemble Program (PROJ):
                                       -> copy from to
				       -> copy Model_creation/binary PROJ_example/funs/model_data
				       -> copy Model_creation/multi PROJ_example/funs/model_data
				       -> copy Model_creation/available_cat.txt PROJ_example/funs
				       -> run program on machine with tcpdump






Folders (all code, with comments):

	Dataset_creation # modify wireshark/editcap path in Dataset_creation/split.py
	Model_creation  
	Program


	


Basic requirements:
	for WM ubuntu/debian python3.8
	for others: ptyhon3.6 or higher (should be mine works fine)
	
	pip install scapy tqdm pandas numpy sklearn (can be deleted manualy)
	
	Additionally: wireshark editcap util
