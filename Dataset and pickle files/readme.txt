File Name:
water_data										: Original dataset used for model building
best_model.pkl									: Optimised SVM model exported from the Colab code
Deployment.py									: Code used to deploy the model on localhost
Sample Data										: Data containing test input values to test the model



To run the deployment:
1. Download Anaconda navigator.
2. Once set up, click on home, and open Jupyter Notebook. 
3. To download all the libraries needed, change directory to where the folder is and run the following command in the terminal
	
	pip install -r requirements.txt

4. To check all the dependencies is successfully installed

	pip list

5. To run deployment, open the "Deployment.py" file in Spyder.
6. Make sure that the sklearn, keras and tensorflow versions on Spyder are the same as those in the FYP notebook.
7. Run the file on Spyder, change the model path to where it is downloaded on your PC. 
8. To deploy on localhost, type "streamlit run (deployment path)/Deployment.py" in the command prompt.


Thanks for reading and have a nice day!
Muzamil Mohammed Ahmed 