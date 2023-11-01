import React, { Fragment, useEffect, useMemo, useRef } from 'react';
import { Card, OverlayTrigger, Popover } from "react-bootstrap";
import { useState } from "react";
import { v4 as uuid } from 'uuid';

export function Temp() {

    // eslint-disable-next-line
    const target = useMemo(() => []);

    const CustomPopover = (item) => {
        return <Popover id="popover-basic" className="stepper-popupover">
            <Popover.Header as="h3">{item.name}</Popover.Header>
            <Popover.Body style={{ height: "auto" }}>
                <ul className='card-body-list'>
                    {item.list.map((i) => <li>{i}</li>)}
                </ul>
            </Popover.Body>
        </Popover >
    };

    const handleClick = () => {
    }


    const stepswizard = [
        {
            name: "Initiation", color: '#3d82c5', indexValue: '', list: [
                'Case initiated',
                `Waiting for JD and MR from Manager/Company`
            ]
        },
        {
            name: "Finalize AD Text, JD, MR And PWR", color: '#682e92', indexValue: 'I',
            list: [
                'Prepare PERM Ad Text, JD and MR',
                'Finalize PERM Ad Text, JD and MR with Company',
                'Prepare Work Experience Chart for Employee to complete',
                'Prepare draft EVL(s) to be obtained by Employee',
                `Receive signed EVL(s) or confirmation that Employee\n
                will be able to obtain EVL(s)`,
                'Prepare PWR for Company\'s review and approval',
                'Submit PWR with DOL'
            ]
        },
        { name: "PWR Pending With DOL", color: '#f7941d', indexValue: 'II', list: ['Awaiting PWD from DOL'] },
        {
            name: "In Recruitment", color: '#272264', indexValue: 'III', list: [
                'Receive PWD from DOL', 'Begin PERM Recruitment'
            ]
        },
        { name: "Quite Period", color: '#46cb09', indexValue: 'IV', list: ['DOL Requirement'] },
        {
            name: "Prepare Case For Filing", color: '#bf1e2e', indexValue: 'V', list: [
                'Receive Recruitment Results Tracker from Company',
                'Receive Recruitment Results Report from Company',
                `Receive Approval from
            Company to Proceed with the Case`,
                `Draft ETA Form 9089 for
            Employee and Company's Review`,
                'Finalize and File ETA Form 9089 with DOL'
            ]
        },
        {
            name: "ETA Firm 9089 Filed And Pending", color: '#026a37', indexValue: 'VI', list: [
                'PERM Application Pending with DOL'
            ]
        },
    ];

    const [activeStep] = useState(1);

    useEffect(() => {
        target.forEach(btn => btn.current.click())
    }, [target])

    const alternatePosition = (index) => index % 2 === 0 ? 'top' : 'bottom'
    const isActiveStep = (index) => index <= activeStep ? 'active' : ''

    return (<Fragment>
        <Card>
            <Card.Body className="ht-700 pd-t-200">
                <div className="track mt-5">
                    {stepswizard.map((item, index) => {
                        target.push(new useRef(null))
                        return <OverlayTrigger
                            key={uuid}
                            trigger="click"
                            placement={alternatePosition(index)}
                            overlay={CustomPopover(item)}
                        >
                            <span className={`icon ${isActiveStep(index)}`} ref={target[index]} onClick={() => handleClick()}>
                                <i className="mdi mdi-arrow-right"></i>
                            </span>
                        </OverlayTrigger>
                    })}
                </div>
            </Card.Body>
        </Card>
    </Fragment>)
};

Temp.propTypes = {};

Temp.defaultProps = {};

export default Temp;