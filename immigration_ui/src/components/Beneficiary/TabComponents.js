import React, { useEffect } from 'react'
import { Card, Col, ListGroup, Row, Table } from 'react-bootstrap'
import { Link, useNavigate, useSearchParams } from 'react-router-dom'
import { v4 as uuidv4 } from 'uuid'
import { useState } from 'react'
import { Popover, Step, StepLabel, Stepper, stepLabelClasses } from '@mui/material'
import { Check } from '@mui/icons-material'
import styled from 'styled-components'
import { useDispatch, useSelector } from 'react-redux'
import { actions } from 'store/slices/beneficiarySlice'
import { beneficiaryService } from 'services/beneficiary.service'
import { SimpleLoader } from 'components/Common/SimpleLoader'
import { textValidator, trimDate } from 'utils/textValidator'

const Tile = ({ item }) => {
    return (
        <div className="tile-content">
            <h5>{item.title}</h5>
            {item.values.map((value) => (
                <div key={uuidv4()} className="d-flex justify-content-between">
                    <span>{value.key}</span>
                    {value.type && value.type === 'link' ? (
                        <a href={value.value} rel="noreferrer" target="_blank">
                            View
                        </a>
                    ) : (
                        <b className="tile-value">{value.value}</b>
                    )}
                </div>
            ))}
        </div>
    )
}

export function BeneficiaryImmigrationTimeline() {
    const dispatch = useDispatch()

    const immigrationTimelineState = useSelector((state) => state.beneficiary.profileData.immigrationTimeline)
    const _id = useSelector((state) => state.beneficiary.profileData.beneficiary.id)
    const [searchParams, _] = useSearchParams()

    const extractData = (leaf) => immigrationTimelineState?.[leaf]

    const stepswizard = [
        { name: 'H-1B Cap Petition', ...extractData('h1b') },
        { name: 'Recent Underlying NIV Petition', ...extractData('runp') },
        { name: 'Recent PERM Application', ...extractData('rpa') },
        { name: 'Recent I-140 Petition', ...extractData('ri140p') },
        { name: 'Recent I-130 Petition', ...extractData('ri130p') },
        { name: 'Recent AOS Application', ...extractData('raosa') }
    ]

    const loadAPI = () => {
        dispatch(actions.setTabLoader({ tab: 'immigrationTimeline', status: true }))
        beneficiaryService.getImmigrationTimeline(_id).then((res) => {
            dispatch(actions.setImmigrationTimeline(res))
        })
    }

    useEffect(() => {
        if (searchParams.get('pane') === '1') {
            loadAPI()
        }
    }, [])

    const [activeStep] = useState(3)

    const StepDetails = ({ className, data }) => {
        searchParams.set('projectID', textValidator(data?.ProjectID))

        const projectLink = `./?${searchParams.toString()}`

        if (className === 'for-popover') {
            return (
                <ul className={`stepper-list ${className}`}>
                    <li>
                        <span>Year Initiated</span>
                        <b>{textValidator(data.YearInitiated)}</b>
                    </li>
                    <li>
                        <span>Year Filed</span>
                        <b>{textValidator(data.YearFiled)}</b>
                    </li>
                    <li>
                        <span>Year Closed</span>
                        <b>{textValidator(data.YearClosed)}</b>
                    </li>
                    <li>
                        <span>Project Status</span>
                        <b>{textValidator(data.ProjectPrimaryStatus)}</b>
                    </li>
                    <li>
                        <span>Project ID</span>
                        <Link to={projectLink}>View</Link>
                    </li>
                </ul>
            )
        } else {
            return (
                <ul className={`stepper-list ${className}`}>
                    <li>
                        <b>{textValidator(data?.YearInitiated)}</b>
                    </li>
                    <li>
                        <Link to={projectLink}>View</Link>
                    </li>
                </ul>
            )
        }
    }

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

    const StepIconComponent = (index, data) => {
        const [anchorEl, setAnchorEl] = React.useState(null)

        const handlePopoverOpen = (event) => {
            setAnchorEl(event.currentTarget)
        }

        const handlePopoverClose = () => {
            setAnchorEl(null)
        }

        const open = Boolean(anchorEl)

        return (
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
                {index <= activeStep ? (
                    <Popover
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
                        transformOrigin={{
                            vertical: 'top',
                            horizontal: 'center'
                        }}
                    >
                        <StepDetails className="for-popover" data={data} />
                    </Popover>
                ) : null}
            </div>
        )
    }

    return immigrationTimelineState?.loading ? (
        <SimpleLoader />
    ) : (
        <Card className="custom-card static-card">
            <Card.Body>
                <h5 className="main-content-label">Beneficiary Immigration Timeline</h5>
                <div className="timeline-stepper-container">
                    <div className="step-fields">
                        <h5>Year Initiated</h5>
                        <h5>Project ID</h5>
                    </div>
                    <Stepper
                        activeStep={activeStep}
                        connector={null}
                        alternativeLabel
                        className="stepper-container mt-5"
                    >
                        {stepswizard.map((step, index) => {
                            return (
                                <Step key={uuidv4()}>
                                    <div style={{ height: '100px' }}>
                                        <CustomStepLabel
                                            index={index}
                                            StepIconComponent={() => StepIconComponent(index, step)}
                                        >
                                            {step.name}
                                        </CustomStepLabel>
                                    </div>
                                    {index <= activeStep ? <StepDetails data={step} /> : null}
                                </Step>
                            )
                        })}
                    </Stepper>
                </div>
            </Card.Body>
        </Card>
    )
}

export function ImmigrationStatusKeyDates() {
    const dispatch = useDispatch()

    const initState = useSelector((state) => state.beneficiary.profileData.immigrationStatusKeyDates)
    const _id = useSelector((state) => state.beneficiary.profileData.beneficiary.id)
    const [searchParams, _] = useSearchParams()

    const loadAPI = () => {
        dispatch(actions.setTabLoader({ tab: 'immigrationStatusKeyDates', status: true }))
        beneficiaryService.getImmigrationStatusKeyDates(_id).then((res) => {
            dispatch(actions.setImmigrationStatusKeyDates(res))
        })
    }

    useEffect(() => {
        if (searchParams.get('pane') === '3') {
            loadAPI()
        }
    }, [])

    const list = {
        group: [
            {
                title: 'Immigration',
                values: [
                    { key: 'Status', value: textValidator(initState?.immigration_status?.ImmigrationStatusType) },
                    { key: 'Status Exp', value: textValidator(trimDate(initState?.immigration_status?.StatusExpDate)) }
                ]
            },
            {
                title: 'I-797',
                values: [
                    { key: 'Approved Date', value: textValidator(trimDate(initState?.i797?.DecisionNoticeDate)) },
                    { key: 'Status', value: textValidator(initState?.i797?.CurrentI797Status) },
                    { key: 'Valid From', value: textValidator(trimDate(initState?.i797?.DecisionNoticeDate)) },
                    { key: 'Exp Date', value: textValidator(trimDate(initState?.i797?.CurrentI797ExpirationDate)) }
                ]
            },
            {
                title: 'I-129S',
                values: [
                    { key: 'End Date', value: textValidator(trimDate(initState?.i129s?.CurrentI797ExpirationDate)) },
                    { key: 'Requested Date', value: textValidator(trimDate(initState?.i129s?.DecisionNoticeDate)) }
                ]
            },
            {
                title: 'U.S. Entry',
                values: [
                    { key: 'Most Recent Entry Date', value: textValidator(trimDate(initState?.us_entry?.EntryDate)) },
                    { key: 'I-94 Number', value: textValidator(trimDate(initState?.us_entry?.I94Number)) }
                ]
            },
            {
                title: 'Visa',
                values: [
                    { key: 'Type', value: textValidator(trimDate(initState?.visa?.VisaClass)) },
                    { key: 'Exp Date', value: textValidator(trimDate(initState?.visa?.ValidTo)) },
                    { key: 'PED', value: textValidator(trimDate(initState?.visa?.VisaPedDate)) }
                ]
            },
            {
                title: 'PR Data',
                values: [
                    {
                        key: 'Re-Entry Permit Exp Date',
                        value: textValidator(trimDate(initState?.pr_data?.PermitExpDate))
                    },
                    { key: 'Green Card Exp Date', value: textValidator(trimDate(initState?.pr_data?.GreenCardExpDate)) }
                ]
            }
        ]
    }

    return initState?.loading ? (
        <SimpleLoader />
    ) : (
        <Card className="custom-card static-card">
            <Card.Body className="">
                <h5 className="main-content-label">Immigration Status & Key Dates</h5>
                <Row className=" row-sm">
                    {list.group.map((item) => {
                        return (
                            <Col md={6} xl={4} className="mb-3 h-185" key={uuidv4()}>
                                <Tile item={item} />
                            </Col>
                        )
                    })}
                </Row>
            </Card.Body>
        </Card>
    )
}

export function OpenCases() {
    const navigate = useNavigate()

    const handleRedirect = (page, caseType) => {
        if (page === 'case-spec') {
            navigate('/case-info/specific', { state: { caseType } })
        }
    }

    return (
        <Card className="custom-card static-card">
            <Card.Body className="">
                <h5 className="main-content-label">Projects</h5>

                <Row className="row-sm">
                    <Col md={4} bg="primary">
                        <Card
                            className="custom-card bg-primary tx-white"
                            onClick={() => handleRedirect('case-spec', 'open')}
                        >
                            <Card.Body>
                                <div className="d-flex align-items-center currency-item">
                                    <div>
                                        <span className="tx-13 mb-3">Open Projects</span>
                                        <h3 className="m-0 mt-2">15</h3>
                                    </div>
                                    <div className="ms-auto mt-auto">
                                        <i className="cf cf-btc" />
                                    </div>
                                </div>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col md={4}>
                        <Card
                            className="custom-card bg-success tx-white"
                            onClick={() => handleRedirect('case-spec', 'open')}
                        >
                            <Card.Body>
                                <div className="d-flex align-items-center currency-item">
                                    <div>
                                        <span className="tx-13 mb-3">Approved Projects</span>
                                        <h3 className="m-0 mt-2">6</h3>
                                    </div>
                                    <div className="ms-auto mt-auto">
                                        <i className="cf cf-btc" />
                                    </div>
                                </div>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col md={4}>
                        <Card
                            className="custom-card bg-danger tx-white"
                            onClick={() => handleRedirect('case-spec', 'open')}
                        >
                            <Card.Body>
                                <div className="d-flex align-items-center currency-item">
                                    <div>
                                        <span className="tx-13 mb-3">Closed Projects</span>
                                        <h3 className="m-0 mt-2">10</h3>
                                    </div>
                                    <div className="ms-auto mt-auto">
                                        <i className="cf cf-btc" />
                                    </div>
                                </div>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Card.Body>
        </Card>
    )
}

export function WorkAuthorizationInfo() {
    const dispatch = useDispatch()
    const initState = useSelector((state) => state.beneficiary.profileData.workAuthorizationInfo)
    const _id = useSelector((state) => state.beneficiary.profileData.beneficiary.id)
    const [searchParams, _] = useSearchParams()

    // data setup

    const [list] = useState({
        group: [
            {
                title: 'Immigration',
                values: [
                    { key: 'Status', value: textValidator(initState?.immigration?.ImmigrationStatusType) },
                    { key: 'Status Exp', value: textValidator(trimDate(initState?.immigration?.StatusExpDate)) }
                ]
            },
            {
                title: 'I-797',
                values: [
                    { key: 'Status', value: textValidator(initState?.i797?.CurrentI797Status) },
                    { key: 'Exp Date', value: textValidator(trimDate(initState?.i797?.CurrentI797ExpirationDate)) }
                ]
            },
            {
                title: 'AOS EAD',
                values: [
                    { key: 'Valid From', value: textValidator(trimDate(initState?.aos_ead?.ValidFrom)) },
                    { key: 'Exp Date', value: textValidator(trimDate(initState?.aos_ead?.ValidTo)) }
                ]
            },
            {
                title: 'NIV EAD',
                values: [
                    { key: 'Type', value: textValidator(trimDate(initState?.niv_ead?.EADTypeID)) }, // BEN_PENDING
                    { key: 'Valid From', value: textValidator(trimDate(initState?.niv_ead?.CurrentNIVEADValidFrom)) },
                    { key: 'Exp Date', value: textValidator(trimDate(initState?.niv_ead?.CurrentNIVEADValidTo)) }
                ]
            }
        ]
    })

    const loadAPI = () => {
        dispatch(actions.setTabLoader({ tab: 'workAuthorizationInfo', status: true }))
        beneficiaryService.getWorkAuthorizationInfo(_id).then((res) => {
            dispatch(actions.setWorkAuthorizationInfo(res))
        })
    }

    useEffect(() => {
        if (searchParams.get('pane') === '5') loadAPI()
    }, [])

    return initState?.loading ? (
        <SimpleLoader />
    ) : (
        <Card className="custom-card static-card">
            <Card.Body className="">
                <h5 className="main-content-label">Work Authorization Info</h5>
                <Row className=" row-sm">
                    {list.group.map((item) => {
                        return (
                            <Col md={6} xl={4} className="mb-3" key={uuidv4()}>
                                <Tile item={item} />
                            </Col>
                        )
                    })}
                </Row>
            </Card.Body>
        </Card>
    )
}

export function BeneficiaryQuickAssessmentForm() {
    const dispatch = useDispatch()
    const formState = useSelector((state) => state.beneficiary.profileData.quickAssessmentForm)
    const _id = useSelector((state) => state.beneficiary.profileData.beneficiary.id)
    const [searchParams, _] = useSearchParams()

    // data setup

    const extractData = (leaf) => textValidator(formState?.beneficiary_details?.[leaf], 'NA')

    const beneficiaryData = {
        title: 'Benificiary Details',
        values: [
            { key: 'Beneficiary Id', value: extractData('BeneficiaryID') },
            { key: 'Employee Id', value: extractData('EmployeeId') },
            { key: 'Employee First Name', value: extractData('FirstName') },
            { key: 'Employee Last Name', value: extractData('LastName') },
            { key: 'Petitioner Name', value: extractData('EmployerName') }
        ]
    }
    const loadAPI = () => {
        dispatch(actions.setTabLoader({ tab: 'quickAssessmentForm', status: true }))
        beneficiaryService.getQuickAssessmentForm(_id).then((res) => {
            dispatch(actions.setQuickAssessmentForm(res))
        })
    }

    useEffect(() => {
        if (searchParams.get('pane') === '2') loadAPI()
    }, [])

    const list = {
        group: [
            {
                title: 'Immigration',
                values: [
                    { key: 'Status', value: textValidator(formState?.immigration?.ImmigrationStatusType) },
                    { key: 'Status Exp', value: textValidator(trimDate(formState?.immigration?.StatusExpDate)) },
                    {
                        key: 'Future Imm Status Effective Date',
                        value: textValidator(trimDate(formState?.immigration?.FutureImmStatusEffectiveDate))
                    }
                ]
            },
            {
                title: 'I-797',
                values: [
                    { key: 'Approved Date', value: textValidator(trimDate(formState?.i797?.DecisionNoticeDate)) },
                    { key: 'Status', value: textValidator(formState?.i797?.CurrentI797Status) },
                    { key: 'Valid From', value: textValidator(trimDate(formState?.i797?.DecisionNoticeDate)) },
                    { key: 'Exp Date', value: textValidator(trimDate(formState?.i797?.CurrentI797ExpirationDate)) }
                ]
            },
            {
                title: 'I-129S',
                values: [
                    { key: 'End Date', value: textValidator(trimDate(formState?.i129s?.CurrentI797ExpirationDate)) },
                    { key: 'Requested Date', value: textValidator(trimDate(formState?.i129s?.DecisionNoticeDate)) }
                ]
            },
            {
                title: 'U.S. Entry',
                values: [
                    { key: 'Most Recent Entry Date', value: textValidator(trimDate(formState?.us_entry?.EntryDate)) },
                    { key: 'I-94 Number', value: textValidator(formState?.us_entry?.I94Number) }
                ]
            },
            {
                title: 'Visa',
                values: [
                    { key: 'Type', value: textValidator(formState?.visa?.VisaClass) },
                    { key: 'Exp Date', value: textValidator(trimDate(formState?.visa?.ValidTo)) },
                    { key: 'PED', value: textValidator(trimDate(formState?.visa?.VisaPedDate)) }
                ]
            },
            {
                title: 'PR Data',
                values: [
                    {
                        key: 'Re-Entry Permit Exp Date',
                        value: textValidator(trimDate(formState?.pr_data?.ReEntryPermitExpirationDate))
                    },
                    {
                        key: 'Green Card Exp Date',
                        value: textValidator(trimDate(formState?.pr_data?.GreenCardExpirationDate))
                    }
                ]
            },
            {
                title: 'Other',
                values: [
                    {
                        key: 'Final NIV Initial H/L Entry',
                        value: textValidator(trimDate(formState?.other1?.FinalNIVInitialHLEntry))
                    },
                    { key: 'Fifth Year Exp', value: textValidator(trimDate(formState?.other1?.FifthYearExp)) },
                    { key: 'NIV Max Out Date', value: textValidator(trimDate(formState?.other1?.NIVMaxOutDate)) }
                ]
            },
            {
                title: 'Other (J-1 Info)',
                values: [
                    {
                        key: 'Subject to TYSH Requirement',
                        value: textValidator(trimDate(formState?.other2?.SubjectToHomeStayRequirement))
                    },
                    {
                        key: 'TYSH Requirement Complied',
                        value: textValidator(trimDate(formState?.other2?.HomeStayRequirementComplied))
                    },
                    {
                        key: 'TYSH Waiver Obtain',
                        value: textValidator(trimDate(formState?.other2?.HomeStayWaiverObtain))
                    },
                    {
                        key: 'DS-2019 Valid To Date',
                        value: textValidator(trimDate(formState?.other2?.['Ds2019ExpirationDate']))
                    }
                ]
            }
        ]
    }

    const rows = formState?.table?.filter((t) => Object.keys(t).length > 0) || []

    return formState?.loading ? (
        <SimpleLoader />
    ) : (
        <Card className="custom-card static-card beneficiaryQuickAssessment">
            <Card.Body>
                <h5 className="main-content-label">Beneficiary Quick Assessment Form</h5>
                <Row className=" row-sm">
                    <Col md={6} xl={4} className="mt-2">
                        <Tile item={beneficiaryData} />
                    </Col>

                    <Col md={6} xl={8} className="mb-3">
                        <Table className="table text-nowrap text-md-nowrap mg-b-0 border">
                            <thead>
                                <tr>
                                    <th>
                                        <b>Doc Type</b>
                                    </th>
                                    <th>
                                        <b>Exp Date</b>
                                    </th>
                                    <th>
                                        <b>
                                            Ext/Ren
                                            <br />
                                            Initiated
                                        </b>
                                    </th>
                                    <th>
                                        <b>
                                            Project Initiated
                                            <br />
                                            Date
                                        </b>
                                    </th>
                                    <th>
                                        <b>
                                            Secondary Project <br />
                                            Status
                                        </b>
                                    </th>
                                    <th>
                                        <b>Project Id</b>
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                {rows.map((item, index) => (
                                    <tr key={index} data-index={index}>
                                        <td>{textValidator(item?.['DocumentType'])}</td>
                                        <td>{textValidator(trimDate(item?.['ExpDate']))}</td>
                                        <td>{textValidator(item?.['ExtRenInitiated'])}</td>
                                        <td>{textValidator(trimDate(item?.['ProjectInitiatedDate']))}</td>
                                        <td>{textValidator(item?.['SecondaryProjectStatus'])}</td>
                                        <td>{textValidator(item?.['ProjectID'])}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </Table>
                    </Col>
                </Row>

                <Row className="row-sm">
                    <Col sm={6} md={6}>
                        <Card className="custom-card">
                            <Card.Body>
                                <div>
                                    <h6 className="main-content-label mb-1">Summary</h6>
                                    <p className="text-muted card-sub-title">
                                        The below summary/assessment is based on responses provided by the Beneficiary
                                        and information currently recorded in the system.
                                    </p>
                                    <Card className="tx-14">
                                        <Card.Body>
                                            <ul className="mb-0">
                                                <li>
                                                    The Beneficiary does not have any "General Eligibility or
                                                    Inadmissibility" related issues.
                                                </li>
                                                <li>
                                                    The above-named Beneficiary is a __________ Beneficiary
                                                    (Primary/Dependent).{' '}
                                                </li>
                                                <li>
                                                    The Beneficiary is subject to NIV Max Out Date and the date is
                                                    ________.{' '}
                                                </li>
                                                <li>
                                                    The Beneficiary _____ (IS/NOT) eligible to extend his/her NIV status
                                                    for the following reasons:
                                                </li>
                                            </ul>
                                        </Card.Body>
                                    </Card>
                                </div>
                                <Card className="custom-card mt-3 border">
                                    <Card.Header className="p-3 tx-medium my-auto tx-white bg-primary">
                                        IS ELIGIBLE TO EXTEND NIV STATUS B/C
                                    </Card.Header>
                                    <Card.Body>
                                        <ul>
                                            <li>Approved I-140 with Current Employer: Yes</li>
                                            <li>Approved I-140 with a subsidiary company of Current Employer: Yes</li>
                                            <li>Approved I-140 from a Prior Employer: Yes</li>
                                        </ul>
                                    </Card.Body>
                                </Card>
                            </Card.Body>
                        </Card>
                    </Col>

                    <Col sm={6} md={6}>
                        <Card className="custom-card static-card">
                            <Card.Body className="">
                                <div className="d-flex justify-content-between">
                                    <h5 className="main-content-label">Immigration Status & Key Dates</h5>
                                </div>
                                <Row className="row-sm">
                                    {list.group.map((item) => {
                                        return (
                                            <Col md={12} xl={6} className="mb-3" key={uuidv4()}>
                                                <Tile item={item} />
                                            </Col>
                                        )
                                    })}
                                </Row>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Card.Body>
        </Card>
    )
}

export function PRProcessInitiationInfo() {
    const dispatch = useDispatch()

    const initState = useSelector((state) => state.beneficiary.profileData.prProcessInfo)
    const _id = useSelector((state) => state.beneficiary.profileData.beneficiary.id)
    const [searchParams, _] = useSearchParams()

    const extractData = (leaf) => initState?.[leaf]

    const loadAPI = () => {
        dispatch(actions.setTabLoader({ tab: 'prProcessInfo', status: true }))
        beneficiaryService.getPRProcessInfo(_id).then((res) => {
            dispatch(actions.setPrProcessInfo(res))
        })
    }

    const list = {
        group1: [
            {
                title: 'PR Process',
                values: [
                    { key: 'Eligible', value: textValidator(extractData('pr_process')?.IsEligiblePRProcess) },
                    {
                        key: 'Initiated',
                        value: textValidator(extractData('pr_process')?.InitiationStartDate ? true : false)
                    },
                    {
                        key: 'Initiation Date',
                        value: trimDate(textValidator(extractData('pr_process')?.InitiationStartDate))
                    },
                    {
                        key: 'Target Start Date',
                        value: trimDate(textValidator(extractData('pr_process')?.TargetStartDate))
                    }
                ]
            }
        ],
        group2: [
            {
                title: 'PERM Project',
                values: [
                    {
                        key: 'Filed Date',
                        value: trimDate(textValidator(extractData('perm_project')?.PermProjectFiledDate))
                    },
                    { key: 'Status', value: textValidator(extractData('perm_project')?.ProjectPrimaryStatus) },
                    {
                        key: 'Project ID',
                        value: textValidator(extractData('perm_project')?.PermProjectID),
                        type: 'link'
                    }
                ]
            },
            {
                title: 'I-140',
                values: [
                    {
                        key: 'Filed Date',
                        value: trimDate(textValidator(extractData('i140')?.['I140ProjectFiledDate']))
                    },
                    { key: 'Status', value: textValidator(extractData('i140')?.['ProjectPrimaryStatus']) },
                    { key: 'Project ID', value: textValidator(extractData('i140')?.['I140ProjectID']), type: 'link' }
                ]
            },
            {
                title: 'I-485',
                values: [
                    { key: 'Filed Date', value: trimDate(textValidator(extractData('i485')?.['AOSProjectFiledDate'])) },
                    { key: 'Status', value: textValidator(extractData('i485')?.['ProjectPrimaryStatus']) },
                    { key: 'Project ID', value: textValidator(extractData('i485')?.['AOSProjectID']), type: 'link' }
                ]
            },
            {
                title: 'I-130',
                values: [
                    {
                        key: 'Filed Date',
                        value: trimDate(textValidator(extractData('i130')?.['I130ProjectFiledDate']))
                    },
                    { key: 'Status', value: textValidator(extractData('i130')?.['ProjectPrimaryStatus']) },
                    { key: 'Project ID', value: textValidator(extractData('i130')?.['I130ProjectID']), type: 'link' }
                ]
            }
        ]
    }

    useEffect(() => {
        if (searchParams.get('pane') === '6') {
            loadAPI()
        }
    }, [])

    return initState.loading ? (
        <SimpleLoader />
    ) : (
        <Card className="custom-card static-card">
            <Card.Body className="">
                <h5 className="main-content-label">PR Process Initiation Info</h5>
                <Row className=" row-sm">
                    {list.group1.map((item) => {
                        return (
                            <Col md={6} xl={4} className="mb-3" key={uuidv4()}>
                                <Tile item={item} />
                            </Col>
                        )
                    })}
                </Row>
                <h5 className="main-content-label my-2">PR Process Status Info</h5>
                <Row className=" row-sm">
                    {list.group2.map((item) => {
                        return (
                            <Col md={4} xl={3} className="mb-3" key={uuidv4()}>
                                <Tile item={item} />
                            </Col>
                        )
                    })}
                </Row>
            </Card.Body>
        </Card>
    )
}

export function EmploymentInfo() {
    const dispatch = useDispatch()
    const initState = useSelector((state) => state.beneficiary.profileData.employeeInfo)
    const _id = useSelector((state) => state.beneficiary.profileData.beneficiary.id)
    const [searchParams, _] = useSearchParams()

    const [list] = useState({
        group: [
            {
                title: '',
                values: [
                    { key: 'Employer Name', value: textValidator(initState?.emp_info_tab1?.EmployerName) },
                    { key: 'Employee ID', value: textValidator(initState?.emp_info_tab1?.EmployeeId) },
                    { key: 'Current Job Title', value: textValidator(initState?.emp_info_tab1?.JobTitle) }
                ]
            },
            {
                title: '',
                values: [
                    {
                        key: 'Works at Multiple Sites?',
                        value: textValidator(initState?.emp_info_tab2?.WorksATMultipleSites)
                    },
                    {
                        key: 'Primary Work Location',
                        value: textValidator(initState?.emp_info_tab2?.PrimaryWorkLocation)
                    },
                    {
                        key: 'Additional Work Locations',
                        value: textValidator(initState?.emp_info_tab2?.AdditionalWorkLocations),
                        type: 'link'
                    }
                ]
            },
            {
                title: '',
                values: [
                    {
                        key: 'Employment Start Date',
                        value: trimDate(textValidator(initState?.emp_info_tab3?.HireDate))
                    },
                    {
                        key: 'Most Recent LCA Number',
                        value: textValidator(initState?.emp_info_tab3?.MostRecentLCANumber)
                    }
                ]
            },
            {
                title: '',
                values: [
                    { key: '', value: '' },
                    { key: '', value: '' },
                    { key: '', value: '', type: '' }
                ]
            },
            {
                title: '',
                values: [
                    { key: '', value: '' },
                    { key: '', value: '' },
                    { key: '', value: '', type: '' }
                ]
            },
            {
                title: '',
                values: [
                    { key: '', value: '' },
                    { key: '', value: '' },
                    { key: '', value: '', type: '' }
                ]
            }
        ]
    })

    const loadAPI = () => {
        dispatch(actions.setTabLoader({ tab: 'employeeInfo', status: true }))
        beneficiaryService.getEmploymentInfo(_id).then((res) => {
            dispatch(actions.setEmployeeInfo(res))
        })
    }

    useEffect(() => {
        if (searchParams.get('pane') === '8') loadAPI()
    }, [])

    return initState?.loading ? (
        <SimpleLoader />
    ) : (
        <Card className="custom-card static-card">
            <Card.Body className="">
                <h5 className="main-content-label">Employment Info</h5>
                <Row className=" row-sm">
                    {list.group.map((item) => {
                        return (
                            <Col md={6} xl={4} className="mb-3 h-185" key={uuidv4()}>
                                <Tile item={item} />
                            </Col>
                        )
                    })}
                </Row>
            </Card.Body>
        </Card>
    )
}

export function PassportTravel() {
    const dispatch = useDispatch()
    const initState = useSelector((state) => state.beneficiary.profileData.passportTravel)
    const _id = useSelector((state) => state.beneficiary.profileData.beneficiary.id)
    const [searchParams, _] = useSearchParams()

    const list = {
        group: [
            {
                title: 'Most Recent Travel',
                values: [
                    { key: 'Type', value: textValidator(initState?.most_recent_travel?.TravelType) },
                    { key: 'Date', value: trimDate(textValidator(initState?.most_recent_travel?.TravelStartDate)) }
                ]
            },
            {
                title: 'Passport',
                values: [
                    { key: 'Number', value: textValidator(initState?.passport?.PassportNumber) },
                    { key: 'Issuing Country', value: textValidator(initState?.passport?.IssuenceCountry) },
                    { key: 'Exp Date', value: trimDate(textValidator(initState?.passport?.ValidTo)) }
                ]
            },
            {
                title: 'Visa',
                values: [
                    { key: 'Type', value: textValidator(initState?.visa?.VisaType) },
                    { key: 'Exp Date', value: trimDate(textValidator(initState?.visa?.ValidTo)) },
                    { key: 'Advance Parole Exp Date', value: trimDate(textValidator(initState?.visa?.ParoleExpDate)) }
                ]
            },
            {
                title: 'Travel Document',
                values: [
                    { key: 'Issuing Country', value: textValidator(initState?.travel_document?.IssuingCountry) },
                    { key: 'Exp Date', value: trimDate(textValidator(initState?.travel_document?.I94ExpirationDate)) }
                ]
            },
            {
                title: 'Upcoming Travel',
                values: [
                    {
                        key: 'Tentive Departure Date',
                        value: trimDate(textValidator(initState?.upcoming_travel?.TentativeDepartureDate))
                    },
                    {
                        key: 'Tentive Arrival Date',
                        value: trimDate(textValidator(initState?.upcoming_travel?.TentativeArrivalDate))
                    }
                ]
            }
        ]
    }

    const loadAPI = () => {
        dispatch(actions.setTabLoader({ tab: 'passportTravel', status: true }))
        beneficiaryService.getPassportTravel(_id).then((res) => {
            dispatch(actions.setPassportTravel(res))
        })
    }

    useEffect(() => {
        if (searchParams.get('pane') === '9') loadAPI()
    }, [])

    return initState?.loading ? (
        <SimpleLoader />
    ) : (
        <Card className="custom-card static-card">
            <Card.Body className="">
                <h5 className="main-content-label">Passport & Travel</h5>
                <Row className=" row-sm">
                    {list.group.map((item) => {
                        return (
                            <Col md={6} xl={4} className="mb-3 h-185" key={uuidv4()}>
                                <Tile item={item} />
                            </Col>
                        )
                    })}
                </Row>
            </Card.Body>
        </Card>
    )
}

export function PersonalData() {
    const dispatch = useDispatch()
    const initState = useSelector((state) => state.beneficiary.profileData.personalInfo)
    const _id = useSelector((state) => state.beneficiary.profileData.beneficiary.id)
    const [searchParams, _] = useSearchParams()

    const list = {
        group: [
            {
                title: 'Birth Info',
                values: [
                    { key: 'Date of Birth', value: trimDate(textValidator(initState?.birth_info?.BirthDate)) },
                    { key: 'City of Birth', value: textValidator(initState?.birth_info?.BirthCity) },
                    { key: 'State of Birth', value: textValidator(initState?.birth_info?.BirthStateProvince) },
                    { key: 'Country of Birth', value: textValidator(initState?.birth_info?.BirthCountry) }
                ]
            },
            {
                title: 'Citizenship',
                values: [
                    { key: 'Primary Country', value: textValidator(initState?.citizenship?.PermPriorityCountry) },
                    { key: 'Other Countries', value: textValidator(initState?.citizenship?.CitizenshipCountry) },
                    {
                        key: 'Country(ies) of Citizenship',
                        value: textValidator(initState?.citizenship?.AllCitizenshipCountries)
                    }
                ]
            },
            {
                title: 'Marital Status',
                values: [
                    { key: 'Marital Status', value: textValidator(initState?.marital_status?.MaritalStatus) },
                    { key: 'Date of Marriage', value: textValidator(initState?.marital_status?.MarriageDate) },
                    { key: 'Date of Divorce', value: textValidator(initState?.marital_status?.DateofDivorce) },
                    { key: 'Number of Dependents', value: textValidator(initState?.marital_status?.NumberofDependents) }
                ]
            },
            {
                title: 'Contact Info',
                values: [
                    { key: 'Primary Email', value: textValidator(initState?.contact_info?.PersonalEmail) },
                    { key: 'Secondary Email', value: textValidator(initState?.contact_info?.WorkEmail) },
                    { key: 'Home Phone', value: textValidator(initState?.contact_info?.HomePhone) },
                    { key: 'Work Phone', value: textValidator(initState?.contact_info?.WorkPhone) },
                    { key: 'Mobile Phone', value: textValidator(initState?.contact_info?.Mobile) }
                ]
            }
        ]
    }

    const loadAPI = () => {
        dispatch(actions.setTabLoader({ tab: 'personalInfo', status: true }))
        beneficiaryService.getPersonalInfo(_id).then((res) => {
            dispatch(actions.setPersonalInfo(res))
        })
    }

    useEffect(() => {
        if (searchParams.get('pane') === '10') loadAPI()
    }, [])

    return initState?.loading ? (
        <SimpleLoader />
    ) : (
        <Card className="custom-card static-card">
            <Card.Body className="">
                <h5 className="main-content-label">Personal Info</h5>
                <Row className=" row-sm">
                    {list.group.map((item) => {
                        return (
                            <Col md={6} xl={4} className="mb-3 h-185" key={uuidv4()}>
                                <Tile item={item} />
                            </Col>
                        )
                    })}
                </Row>
            </Card.Body>
        </Card>
    )
}

export function PriorityData() {
    const dispatch = useDispatch()

    const initState = useSelector((state) => state.beneficiary.profileData.prPriorityInfo)
    const _id = useSelector((state) => state.beneficiary.profileData.beneficiary.id)
    const [searchParams, _] = useSearchParams()

    const tableData = initState?.priority_info_table || []

    const list = {
        group: [
            {
                title: 'AOS Filing Status',
                values: [
                    {
                        key: 'Filed Date',
                        value: textValidator(trimDate(initState?.aos_filing_status?.ProjectFiledDate))
                    },
                    {
                        key: 'Primart Project Status',
                        value: textValidator(trimDate(initState?.aos_filing_status?.ProjectPrimaryStatus))
                    },
                    {
                        key: 'Secondary Project Status',
                        value: textValidator(trimDate(initState?.aos_filing_status?.ProjectSecondaryStatusID))
                    },
                    { key: 'AOS Project ID', value: textValidator(trimDate(initState?.aos_filing_status?.ProjectID)) },
                    { key: 'Link', value: 'icon link', type: 'link' }
                ]
            },
            {
                title: 'AOS Filing Eligibility- Current',
                values: [
                    {
                        key: 'Month',
                        value: textValidator(trimDate(initState?.aos_filing_eligibility_current?.FilingMonth))
                    },
                    {
                        key: 'Visa Bulletin URL',
                        value: 'https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin/2023/visa-bulletin-for-march-2023.html',
                        type: 'link'
                    },
                    {
                        key: 'Final Action',
                        value: textValidator(trimDate(initState?.aos_filing_eligibility_current?.FinalAction))
                    },
                    {
                        key: 'Dates for Filing',
                        value: textValidator(trimDate(initState?.aos_filing_eligibility_current?.FilingDate))
                    }
                ]
            },
            {
                title: 'AOS Filing Eligibility- Upcoming',
                values: [
                    {
                        key: 'Month ',
                        value: textValidator(trimDate(initState?.aos_filing_eligibility_upcoming?.FilingMonth))
                    },
                    {
                        key: 'Visa Bulletin URL',
                        value: 'https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin/2023/visa-bulletin-for-april-2023.html',
                        type: 'link'
                    },
                    {
                        key: 'Final Action',
                        value: textValidator(trimDate(initState?.aos_filing_eligibility_upcoming?.FilingMonth))
                    },
                    {
                        key: 'Dates for Filing',
                        value: textValidator(trimDate(initState?.aos_filing_eligibility_upcoming?.FilingMonth))
                    }
                ]
            }
        ]
    }

    const loadAPI = () => {
        dispatch(actions.setTabLoader({ tab: 'prProcessInfo', status: true }))
        beneficiaryService.getPriorityInfo(_id).then((res) => {
            dispatch(actions.setPrPriorityInfo(res))
        })
    }

    useEffect(() => {
        if (searchParams.get('pane') === '7') {
            loadAPI()
        }
    }, [])

    return initState.loading ? (
        <SimpleLoader />
    ) : (
        <Card className="custom-card static-card">
            <Card.Body className="priority-info-card">
                <h5 className="main-content-label">Priority Info</h5>
                <Row className=" row-sm">
                    {list.group.map((item) => {
                        return (
                            <Col md={6} xl={4} className="mb-3 h-185" key={uuidv4()}>
                                <Tile item={item} key={uuidv4()} />
                            </Col>
                        )
                    })}
                </Row>
                <Row className="row-sm table-row">
                    <Table border={1}>
                        <thead>
                            <th>Project Type</th>
                            <th>Is Most Recent</th>
                            <th>Is Prior Employer I-140</th>

                            <th>Petitioner Name</th>
                            <th>Sponser Name</th>
                            <th>Priority Date</th>

                            <th>Priority Category</th>
                            <th>Priority Country</th>
                            <th>Underlying PERM Project No</th>
                            <th>Project Receipt No</th>

                            <th>Project Status</th>
                            <th>Project Created Date</th>
                            <th>Project ID / Link</th>
                        </thead>
                        <tbody>
                            {tableData.map((tr) => (
                                <tr>
                                    <td>{textValidator(tr.ProjectType)}</td>
                                    <td>{textValidator(tr?.ISMostRecent)}</td>
                                    <td>{textValidator(tr?.isPriorEmployer)}</td>

                                    <td>{textValidator(tr?.ProjectPetitionName)}</td>
                                    <td>{textValidator(tr?.SponserName)}</td>
                                    <td>{trimDate(textValidator(tr?.ProjectPriorityDate))}</td>

                                    <td>{textValidator(tr?.ProjectPriorityCategory)}</td>
                                    <td>{textValidator(tr?.ProjectPriorityCountry)}</td>
                                    <td>{textValidator(tr?.UnderlyingPermReceiptNumber)}</td>
                                    <td>{textValidator(tr?.ReceiptNumber)}</td>

                                    <td>{textValidator(tr?.ProjectPrimaryStatus)}</td>
                                    <td>{trimDate(textValidator(tr?.CreatedDate))}</td>
                                    <td>
                                        <a href="https://google.com" rel="noreferrer" target={'_blank'}>
                                            A54154785A
                                        </a>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </Table>
                </Row>
            </Card.Body>
        </Card>
    )
}

export function DMSWorkspaceLink() {
    return (
        <Card className="custom-card static-card">
            <Card.Body className="">
                <h5 className="main-content-label">DMS Workspace Link</h5>
            </Card.Body>
        </Card>
    )
}
