import React from "react";
import './Button.css'

export function Button({
    onClick,
    classButton,
    text
}){

    return (
        <button onClick={onClick} className={classButton}>
           {text} 
        </button>
    );
};