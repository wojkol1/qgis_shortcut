class MyEventFilter(QObject):
    def turn_orto(self,lyr):
        if QgsProject.instance().layerTreeRoot().findLayer(lyr.id()).isVisible():
            QgsProject.instance().layerTreeRoot().findLayer(lyr.id()).setItemVisibilityChecked(False)
        else:
            QgsProject.instance().layerTreeRoot().findLayer(lyr.id()).setItemVisibilityChecked(True)
    def eventFilter(self, obj, event):
        """ 
        obj : QObject whose event is intercepted 
        event: QEvent received
        
        returns:
            bool: True to intercept the event, False to forward it
        """
        if event.type() == QEvent.KeyRelease:
            if event.key() == Qt.Key_1:
                iface.setActiveLayer(pwd)
                return True
            elif event.key() == Qt.Key_2:
                iface.setActiveLayer(plc)
                return True
            elif event.key() == Qt.Key_R:
                self.turn_orto(orto)
                return True
            elif event.key() == Qt.Key_D:
                self.turn_orto(dz)
                return True
            elif event.key() == Qt.Key_F:
                self.turn_orto(uw)
                return True
            elif event.key() == Qt.Key_X:
                iface.setActiveLayer(zas)
                return True
            elif event.key() == Qt.Key_Z:
                iface.setActiveLayer(arm)
                return True
        return False
    

# Create and install the event filter on the QgsMapCanvas
pwd= QgsProject.instance().mapLayersByName('Przewody wodociągowe')[0]
plc= QgsProject.instance().mapLayersByName('Przyłącza wodociągowe')[0]

orto= QgsProject.instance().mapLayersByName('Google Hybrid')[0]
dz= QgsProject.instance().mapLayersByName('dzialki_polaczone_rzeszow')[0]

zas= QgsProject.instance().mapLayersByName('Zasuwy na przyłączach')[0]
arm= QgsProject.instance().mapLayersByName('Armatura zaporowa')[0]

eventFilter = MyEventFilter()
iface.mapCanvas().installEventFilter(eventFilter)
#iface.mapCanvas().removeEventFilter(eventFilter)



