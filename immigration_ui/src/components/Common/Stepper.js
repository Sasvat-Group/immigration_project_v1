import React from 'react'
import { v4 as uuidv4 } from 'uuid'
import 'components/Common/Stepper.style.scss'

export default function Stepper({ data, allowList = false }) {

    /* Set 'inherit' as color value if missing in props */
    const getColor = (color) => color !== undefined ? color : 'inherit'

    /* Set step face down side */
    const isAlternate = (index) => index % 2 === 0 ? '' : 'alternate'

    /* StepBadge: Used to show circle with vertical line design */
    /* ----------------------------------------------------- */
    const StepBadge = ({ step, index }) => <div className="step-badge-box">
        <div className={`step-badge ${isAlternate(index)}`}>
            <div className="circle" style={{ backgroundColor: getColor(step.color) }}>{step.indexValue}</div>
            <div className="vertical-line" style={{ borderColor: getColor(step.color) }}></div>
        </div>
    </div>
    /* ----------------------------------------------------- */

    /* StepDown: Used to show bottom card portion of step */
    /* ----------------------------------------------------- */
    const StepDown = ({ options }) => <ul className={`card-body-list ${options.index % 2 === 0 ? 'mt-2' : ''}`} style={{ backgroundColor: '#d2dbf9' }}>
        {options.step.list.map((item, index) => <li key={uuidv4()}>{item}</li>)}
    </ul>
    /* ----------------------------------------------------- */

    return (
        <React.Fragment>
            <div className="stepper-container">
                <div className="box-container">
                    {data.map((step, index) => (
                        <React.Fragment key={uuidv4()}>
                            <div className={`step-box ${isAlternate(index)}`}>
                                <StepBadge step={step} index={index} />
                                <div className="step-hook">
                                    <div className={index !== data.length - 1 ? "horizontal-line" : ""}></div>
                                    <div className="step-hook-body" style={{ backgroundColor: getColor(step.color) }}>
                                        <div className="step-name">{step.name}</div> <i className="icon fas fa-arrow-right"></i>
                                    </div>
                                </div>
                                <div className="step-down-box">
                                    <div className={index % 2 === 0 ? "up-arrow" : "down-arrow mb-2"}></div>
                                    {allowList ?
                                        <StepDown options={{ step, index }} />
                                        : null
                                    }
                                </div>
                            </div>
                        </React.Fragment>
                    ))}
                </div>
            </div>

        </React.Fragment>
    )
}