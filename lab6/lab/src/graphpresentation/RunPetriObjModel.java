/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package graphpresentation;

import PetriObj.PetriObjModel;
import PetriObj.PetriP;
import PetriObj.PetriSim;
import PetriObj.PetriT;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

/**
 *
 * @author Inna
 */
public class RunPetriObjModel extends PetriObjModel{
    
    public RunPetriObjModel(ArrayList<PetriSim> list){
        super(list); 
    }
    
    @Override
        public void go(double timeModeling) { //виведення протоколу подій та результатів моделювання у об"єкт класу JTextArea
        System.out.println(" Events protocol ");
        super.setSimulationTime(timeModeling);

        super.setCurrentTime(0.0);
        double min;
        super.getListObj().sort(PetriSim.getComparatorByPriority()); //виправлено 9.11.2015, 12.10.2017
        for (PetriSim e : super.getListObj()) {
            e.input();
        }
        this.printMark();
        ArrayList<PetriSim> conflictObj = new ArrayList<>();
        Random r = new Random();

        while (super.getCurrentTime() < super.getSimulationTime()) {

            conflictObj.clear();

            min = Double.MAX_VALUE;  //пошук найближчої події

            for (PetriSim e : super.getListObj()) {
                if (e.getTimeMin() < min) {
                    min = e.getTimeMin();
                }
            }
            if (super.isStatistics() == true) {
                for (PetriSim e : super.getListObj()) {
                    if (min > 0) {
                        if (min < super.getSimulationTime()) {
                            e.doStatistics((min - super.getCurrentTime()) / min); //статистика за час "дельта т", для спільних позицій потрібно статистику збирати тільки один раз!!!
                        } else {
                            e.doStatistics((timeModeling - super.getCurrentTime()) / super.getSimulationTime());
                        }
                    }
                }
            }

            super.setCurrentTime(min); // просування часу

            printInfo(" \n Time progress: time = " + super.getCurrentTime() + "\n");

            if (super.getCurrentTime() <= timeModeling) {

                for (PetriSim e : super.getListObj()) {
                    if (super.getCurrentTime() == e.getTimeMin()) { // розв'язання конфлікту об'єктів рівноймовірнісним способом

                        conflictObj.add(e);                           //список конфліктних обєктів
                    }
                }
                int num;
                int max;
                if (super.isProtocolPrint() == true) {
                    printInfo("  List of conflicting objects  " + "\n");
                    for (int ii = 0; ii < conflictObj.size(); ii++) {
                        printInfo("  K [ " + ii + "  ] = " + conflictObj.get(ii).getName() + "\n");
                    }
                }

                if (conflictObj.size() > 1) { //вибір обєкта, що запускається
                    max = conflictObj.size();
                    super.getListObj().sort(PetriSim.getComparatorByPriority());
                    for (int i = 1; i < conflictObj.size(); i++) { //System.out.println("  "+conflictObj.get(i).getPriority()+"  "+conflictObj.get(i-1).getPriority());
                        if (conflictObj.get(i).getPriority() < conflictObj.get(i - 1).getPriority()) {
                            max = i - 1;
                            break;
                        }
                    }
                    if (max == 0) {
                        num = 0;
                    } else {
                        num = r.nextInt(max);
                    }
                } else {
                    num = 0;
                }

                printInfo(" Selected object  " + conflictObj.get(num).getName() + "\n" + " NextEvent " + "\n");

                for (PetriSim list : super.getListObj()) {
                    if (list.getNumObj() == conflictObj.get(num).getNumObj()) {
                        printInfo(" time =   " + super.getCurrentTime() + "   Event '" + list.getEventMin().getName() + "'\n" + "                       is occuring for the object   " + list.getName() + "\n");
                        list.doT();
                        list.output();
                    }
                }
                printInfo("Markers leave transitions:");
                this.printMark();
                Collections.shuffle(getListObj()); // added by Inna 11.07.2018, need for correct functioning of Petri object's shared resource 
                
                getListObj().sort(PetriSim.getComparatorByPriority());
               
                for (PetriSim e : super.getListObj()) {
                        e.input(); //вхід маркерів в переходи Петрі-об'єкта
                }

                printInfo("Markers enter transitions:");
                this.printMark();
            }
        }
       System.out.println("\n Modeling results: \n");

        for (PetriSim e : super.getListObj()) {
            System.out.println("\n Petri-object " + e.getName());
            System.out.println("\n Mean values of the quantity of markers in places : ");
            for (PetriP P : e.getListPositionsForStatistica()) {
                System.out.println("\n  Place '" + P.getName() + "'  " + Double.toString(P.getMean()));
            }
            System.out.println("\n Mean values of the quantity of active transition channels : ");
            for (PetriT T : e.getNet().getListT()) {
                System.out.println("\n Transition '" + T.getName() + "'  " + Double.toString(T.getMean()));
            }
        }
    }

    
     /**
     * Prints the string in given JTextArea object
     *
     * @param info string for printing
     * 
     */
    public void printInfo(String info){
        if(isProtocolPrint() == true)
            System.out.println(info);
    }
    /**
     * Prints the quantity for each position of Petri net
     ** 
     */
    public void printMark(){
        if (isProtocolPrint() == true) {
            for (PetriSim e : super.getListObj()) {
                e.printMark();
            }
        }
    }
}
