import React, { useState, useEffect } from "react";
import step1 from "../../icons/step1.svg";
import LoginButton from "../../../../searchify/src/components";

const Step1 = () => {
  return (
    <div>
      <div className="step">
        <h2>Step 1</h2>
        <LoginButton />
        <img className="stepviz" src={step1} alt="step1" />
      </div>
    </div>
  );
};

export default Step1;
