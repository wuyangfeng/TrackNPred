from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from view.view import TrackNPredView
from control.controller import Controller
from model.model import TnpModel

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()


    view = TrackNPredView() ## Define view
    controller = Controller() ## Define controller
    
    ## to get attributes
    ## Setup the UI of the Dialog using the Class TrackNPredView
    view.setupUi(Dialog) 
    controller.setView(view)

    ##- Set the model using Class Controller
    model = TnpModel(controller) ## model = TnpModel(Controller()) - Select the model
    controller.setModel(model) ## controller.setModel(TnpMdel(Controller())) - Set the model

    #show ui
    Dialog.show()
    sys.exit(app.exec_())