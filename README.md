
# Juice Labs PyTorch+yolov5 Example

**How do I setup and run the PyTorch yolov5 example with Anaconda?**

- Install [Anaconda](https://www.anaconda.com/)
- Clone [Juice-Labs/yolo](https://github.com/Juice-Labs/yolo) from `git@github.com:Juice-Labs/yolo.git`

All of the following steps are run from an Anaconda Prompt from within the directory that you cloned Juice-Labs/yolo to.

Create an Anaconda environment and install PyTorch and yolov5 dependencies by running the following from the cloned repository:

~~~
conda env create -n yolo --file environment.yml
conda activate yolo
pip install -r requirements.txt
~~~

Run yolov5 with native CUDA from the Anaconda Prompt, or with the Juice GPU if you've run the installer and the path containing `python.exe` is listed as active in the `%LocalAppData%\Juice\juice.cfg`:

~~~
python yolo.py
~~~

Run yolov5 through the Juice GPU from the Anaconda Prompt with the path to `juicify.exe` (included in `JuiceClient.zip`) in `PATH`:

~~~
juicify.exe %USERPROFILE%\anaconda3\envs\yolo\python.exe yolo.py
~~~
