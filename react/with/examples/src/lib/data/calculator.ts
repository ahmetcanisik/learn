import {OperatorsType} from "@/lib/types";

export const operators: OperatorsType[] = [
    {
        operatorIcon: "+",
        operatorName: "addition",
        execute: (s1: number = 0, s2: number = 0) => s1 + s2
    },
    {
        operatorIcon: "-",
        operatorName: "subtract",
        execute: (s1: number = 0, s2: number = 0) => s1 - s2
    },
    {
        operatorIcon: "*",
        operatorName: "multiply",
        execute: (s1: number = 0, s2: number = 0) => s1 * s2
    },
    {
        operatorIcon: "/",
        operatorName: "divide",
        execute: (s1: number = 0, s2: number = 0) => s1 / s2
    }
];