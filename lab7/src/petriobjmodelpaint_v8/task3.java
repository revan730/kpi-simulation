import LibNet.NetLibrary;
import PetriObj.ExceptionInvalidNetStructure;
import PetriObj.ExceptionInvalidTimeDelay;
import PetriObj.PetriObjModel;
import PetriObj.PetriSim;

import java.util.ArrayList;

public class task3 {

    public static void main(String[] args) throws ExceptionInvalidNetStructure, ExceptionInvalidTimeDelay {
        PetriObjModel model = getModel();
        model.setIsProtokol(false);
        double timeModeling = 1000;
        model.go(timeModeling);

        System.out.println("Lost Profit:");
        System.out.println(model.getListObj().get(1).getNet().getListP()[1].getMark());
    }

    public static PetriObjModel getModel() throws ExceptionInvalidTimeDelay, ExceptionInvalidNetStructure {

        ArrayList<PetriSim> list = new ArrayList<>();

        list.add(new PetriSim(NetLibrary.CreateNettask3full_1()));
        list.add(new PetriSim(NetLibrary.CreateNettask3full_2()));
        list.add(new PetriSim(NetLibrary.CreateNettask3full_3()));

        list.get(0).getNet().getListP()[2] = list.get(1).getNet().getListP()[0];
        list.get(1).getNet().getListP()[7] = list.get(2).getNet().getListP()[0];

        PetriObjModel model = new PetriObjModel(list);

        return model;
    }
}
