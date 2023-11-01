import { Check } from '@mui/icons-material'
import { Popover, Step, StepLabel, stepLabelClasses, Stepper, popoverClasses, paperClasses } from '@mui/material'
import React, { Fragment } from 'react'
import { useState } from 'react'
import { Button, Card, Dropdown } from 'react-bootstrap'
import { Zoom, toast } from 'react-toastify'
import { projectService } from 'services/project.service'
import styled from 'styled-components'
// import StepZilla from "react-stepzilla";
import { v4 as uuidv4 } from 'uuid'

const Test = () => {
    return (
        <Fragment>
            <div>
                <section className="pt-3">{/* <h5>Test 0</h5> */}</section>
            </div>
        </Fragment>
    )
}

const stepswizard = [
    { name: "Sent Email, Q're, and Docs", component: <Test /> },
    { name: 'Received Completed', component: <Test /> },
    { name: 'Petition/Application Drafted', component: <Test /> },
    { name: 'Sent for Review/Signature', component: <Test /> },
    { name: 'Received Signed Docs', component: <Test /> },
    { name: 'Project Filed & Sent', component: <Test /> },
    { name: 'Received Receipt Notice', component: <Test /> },
    { name: 'Received Decision Notice', component: <Test /> },
    { name: 'Sent Decision Notice', component: <Test /> }
]

const AccordionWizardForm = ({ row }) => {
    // eslint-disable-next-line no-unused-vars
    const [activeStep, setActiveStep] = useState(3)

    const CustomStepLabel = styled(StepLabel)(({ index }) => ({
        [`&.${stepLabelClasses.root}`]: {
            [`&.${stepLabelClasses.alternativeLabel}`]: {
                flexDirection: index % 2 === 0 ? 'column' : 'column-reverse'
            },
            [`.${stepLabelClasses.labelContainer}`]: {
                [`.${stepLabelClasses.label}`]: {
                    marginBottom: '1rem'
                }
            }
        }
    }))

    const StepIconComponent = (index) => {
        const [anchorEl, setAnchorEl] = React.useState(null)

        const handlePopoverOpen = (event) => {
            setAnchorEl(event.currentTarget)
        }

        const handlePopoverClose = () => {
            setAnchorEl(null)
        }

        const open = Boolean(anchorEl)

        const CustomPopover = styled(Popover)(() => ({
            [`&.${popoverClasses.root}`]: {
                [`.${paperClasses.root}`]: {
                    padding: '.5rem .8rem',
                    backgroundColor: `${index % 2 === 0 ? '#6259ca' : '#ec3487'}`,

                    [`&.${paperClasses.elevation}.${paperClasses.rounded}`]: {
                        backgroundColor: `${index % 2 === 0 ? '#6259ca' : '#ec3487'} !important`
                    }
                }
            }
        }))

        const hideIcon = () =>
            (row?.caseId == 2883 || row?.caseId == 2887) && (index === 7 || index === 8) ? true : false

        return hideIcon() ? null : (
            <div>
                <div
                    className={`step-icon-bg ${index <= activeStep ? 'active' : null}`}
                    style={{
                        backgroundColor: `${index % 2 === 0 ? '#6259ca' : '#ec3487'}`
                    }}
                    aria-owns={open ? 'mouse-over-popover' : undefined}
                    aria-haspopup="true"
                    // onClick={handlePopoverOpen}
                    onMouseEnter={handlePopoverOpen}
                    onMouseLeave={handlePopoverClose}
                >
                    <Check />
                </div>
                <CustomPopover
                    id="mouse-over-popover"
                    sx={{
                        pointerEvents: 'none'
                    }}
                    open={open}
                    anchorEl={anchorEl}
                    onClose={handlePopoverClose}
                    disableRestoreFocus
                    anchorOrigin={{
                        vertical: 'bottom',
                        horizontal: 'center'
                    }}
                    className="milestone-popupover"
                    transformOrigin={{
                        vertical: 'top',
                        horizontal: 'center'
                    }}
                >
                    {index <= activeStep ? 'Completed Date: 04-25-2023' : 'Estimated Date: 05-28-2023'}
                </CustomPopover>
            </div>
        )
    }

    return (
        <div className="step-progress">
            <Stepper activeStep={2} connector={null} alternativeLabel className="stepper-container mt-5">
                {stepswizard.map((step, index) => (
                    <Step key={uuidv4()}>
                        <div style={{ height: '200px' }}>
                            <CustomStepLabel
                                index={index}
                                StepIconComponent={() => StepIconComponent(index, step.ProjectID)}
                            >
                                {step.name}
                            </CustomStepLabel>
                        </div>
                    </Step>
                ))}
            </Stepper>
            {/* <StepZilla steps={stepswizard} startAtStep={1} showNavigation={false} /> */}
        </div>
    )
}

const Milestone = ({ row }) => {
    const [secondaryStatus, setSecondaryStatus] = useState('Open')

    const handleActivate = () => {
        projectService.rpaProcessActivate().then((res) => {
            console.log(res)
            toast.success(<p className="mx-2 tx-16 d-flex flex-column align-items-start mb-0">Process Activated</p>, {
                position: toast.POSITION.TOP_CENTER,
                transition: Zoom,
                autoClose: 1500
            })
        })
    }

    return (
        <Fragment>
            <Card className="custom-card">
                <Card.Body className="milestone-card">
                    <label className="main-content-label">Project Milestone</label>
                    <div className="checkout-steps wrapper mt-4">
                        <div id="specic-data-stepper">
                            <AccordionWizardForm row={row} />
                        </div>
                    </div>
                    <div className="d-flex justify-content-between">
                        <Dropdown>
                            <Dropdown.Toggle variant="primary">
                                Secondary Status - {secondaryStatus} <i className="fa fa-pencil mx-2"></i>
                            </Dropdown.Toggle>
                            <Dropdown.Menu style={{ marginTop: '0px' }}>
                                <Dropdown.Item onClick={() => setSecondaryStatus('Open')}>Open</Dropdown.Item>
                                <Dropdown.Item onClick={() => setSecondaryStatus('Approved')}>Approved</Dropdown.Item>
                                <Dropdown.Item onClick={() => setSecondaryStatus('Closed')}>Closed</Dropdown.Item>
                            </Dropdown.Menu>
                        </Dropdown>
                        <Button variant="primary" value="Activate" onClick={handleActivate}>
                            Activate
                        </Button>
                    </div>
                </Card.Body>
            </Card>
        </Fragment>
    )
}

Milestone.propTypes = {}

Milestone.defaultProps = {}

export default Milestone
