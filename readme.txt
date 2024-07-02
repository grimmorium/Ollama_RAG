This is a description (valid on 2024.07.01) on how to create a local LLM bot based on LLAMA3 in two flavours:
1. Chatbot
2. with RAG - supporting documents search 

how to install:

1. go to ollama.com and download ollama for windows (tested on ver 0.1.46 and 0.1.48 [virtual Win11])
2. install ollama
3. go to python.org and download Python (tested on varsion 3.11.5 and 3.12.4 [virtual Win11])
4. install Python
	!!! IMPORTANT !!!
	I. at the beginning of the installation, in one screen tick two checkboxes:
		- "use admin privileges..."
		- "add python to PATH"
	II. at the end of the installation run "Disable PATH limit" function
5. run the windows command line and in it run command: ollama pull dolphin-llama3:8b  (this will download the LLM model. it will download aprox. 4,7GB of data)
6. install the needed packages (run the commands one by one in windows command line):
	- pip install streamlit
	- pip install langchain_core
	- pip install langchain_community
	- pip install streamlit_chat
	- pip install pypdf
	- pip install fastembed
	- pip install chromadb
7. download files: chatbot.py, documentsSearch.py, rag.py, run_chat.bat, run_doc.bat and store them in one folder
8. test if ollama works and if it is capable of running the model:
	a. in windows command line run command "ollama run dolphin-llama3:8b"
	b. when the question prompt appears ask a simple question like "what is 2 squared?"
	c. if the model answers then the installation works
	d. to quit write in the question prompt command "/bye"
	

how to run:
!! information !!
	I. during the first attemts of running, the script may first indicate that there are missing packeges not installed in the system, install them using pip (it may be helpfull to use flag "--only-binary :all:" when using pip and/or indicate specyfic versions)
	II. when all needed packages are installed then at the first run the script will ask you to type in your email (you can skip it by hitting the enter key)

1. run the windows command line
2. go to the folder where the downloaded files are saved
3a. for the Document Search (with RAG) bot run file run_doc.bat
3b. for a classic chatbot run file run_chat.bat

If run correctly then a webbrowser with a chat window will be shown automatically and you can start to use it.


appendix:
- file hardware.txt stores the hardware configuration on which the installation was performed/tested and file packages_list.txt stores the full list of installed python packages on which the installation was performed/tested on this hardware
- file packets_virtual_win11.txt stores the full list of installed python packages on which the installation was performed/tested on a Windows 11 virtual machine - this was a clean installation on a fresh system.



