This is a description (valid on 2024.07.01) on how to create a local LLM based bot on LLAMA3 in two flavours:
1. Chatbot
2. with RAG - supporting documents search 

how to install:

1. goto ollama.com and download ollama for windows (tested on ver 0.1.46)
2. install ollama
3. download files: chatbot.py, documentsSearch.py, rag.py, run_chat.bat, run_doc.bat and store them in one foder

how to run:
!! information !!
	I. during the first attemts of running, the script will first indicate that there are missing packeges not installed in the system, install them using pip (it may be helpfull to use flag "--only-binary :all:" when using pip and/or indicate specyfic versions)
	II. when all needed paskages are installed then the script will download the missing LLAMA3 LLM files (aprox 4,7 GB).

1. run the command line
2. go to the folder where the downloaded files are saved
3a. for the Document Search (with RAG) bot run file run_doc.bat
3b. for a classic chatbot run file run_chat.bat

If run correctly then a webbrowser with a chat window will be shown automatically and you can start to use it.


appendix:
- file hardware.txt stores the hardware configuration on which the installation was performed/tested
- file packages_list.txt stores the full list of installed python packages on which the installation was performed/tested



