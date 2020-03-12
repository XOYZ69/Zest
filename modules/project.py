from modules.version_control import Project
from modules.system import File, System
from modules.style import Style
from modules.algorythms import Algotythms
from .neural_network import NeuralNetwork, NeuralLayer, NeuralLayerStacks
from numpy import exp, array, random, dot
from numpy.core.tests.test_mem_overlap import xrange
import numpy
from tqdm import tqdm


# Initialize Project Objects
project = Project('image_upscaler', 'XOYZ-Code [xoyz.productions@gmail.com]')
project.initialize_project_build()
statistics = project.Statistics()
statistics.update_stat('Project Version', project.project_version_str)
file = File()
system = System('data/system/config.dll')
style = Style()
algorythms = Algotythms(project, statistics)
project.log('Sucessfully initialized all needed Project objects')