import React from "react";
import './Link.css'

export function Link({href, text}){
    return (
        <div>
            <a href={href} target="_blank" className="forgot-link">{text}</a>
        </div >
    );
};