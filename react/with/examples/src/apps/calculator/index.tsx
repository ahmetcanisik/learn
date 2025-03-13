'use client';
import {ResultType} from "@/lib/types";
import {operators} from "@/lib/data";
import {useState} from "react";

function Calculator() {
    // for the calculator result.
    const [result, setResult] = useState<ResultType>({
        first: 0,
        second: 0,
    });

    const [resultScreen, setResultScreen] = useState("0");

    /*const updateResult = ({ first, second }: { first?: number; second?: number; }) => {
        
    }*/

    const updateResultScreen = (innerText: string) => {
        setResultScreen(resultScreen === "0" ? innerText : resultScreen + innerText);
    }

    const onClickOperators = (operator: string) => {
        setResult({
            first: Number(resultScreen),
            second: 0,
        });
        updateResultScreen(operator);
    }

    /*const calculateResult = () => {
        updateResultScreen()
    }*/

    return (
        <div>
            <div className="result-screen">{resultScreen}</div>
            <div>
                {
                    [1,2,3,4,5,6,7,8,9].map((letter) => (
                        <button onClick={() => updateResultScreen(letter.toString())}>{letter}</button>
                    ))
                }
            </div>
            <div>
                {
                    operators.map((operator) => (
                        <button onClick={() => onClickOperators(operator.operatorIcon)} title={operator.operatorName}>{operator.operatorIcon}</button>
                    ))
                }
            </div>
            <button onClick={() => setResultScreen((result.first + result.second).toString())}>=</button>
        </div>
    );
}

export default Calculator;