import React from "react";
import './Input.css'

export function Input({text, type, nameId, placeholder, ...props}){
    let lastStyle = ""
    if ('last' in props){
        lastStyle = "input-last-row"
    } 
    return (
        <>
            <div className="description-by-text">
                <label className="label" htmlFor={nameId}>
                    {text}
                </label>
            </div>
            
            <div className={`input-row ${lastStyle}`}>
                <input type={type} id={nameId} className={'input'} placeholder={placeholder} />
            </div>
        </>

    );
};