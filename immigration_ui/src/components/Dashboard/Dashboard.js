import React, { Fragment, useEffect, useState } from "react"
import { Row, Col, Button, Modal } from "react-bootstrap"
import { useDispatch, useSelector } from "react-redux"
import { setInitialData, setLoading } from "store/slices/dashboardSlice"

import PageHeader from "layouts/PageHeader/PageHeader"
import { CaseGraphs, OverviewTiles, OpenCasesListView, CustomTileView } from "components/Dashboard/UserDashboard"
import { dashboardService } from "services/dashboard.service"
import FullScreenLoader from "components/Common/FullScreenLoader"
import { useLocation, useNavigate } from "react-router-dom"

function Dashboard() {

    /* ====================== Hooks ===================== */

    const [showModal, setModal] = useState(false)
    const [renameModal, setRenameModal] = useState(false)
    const dispatch = useDispatch()
    const location = useLocation()
    const navigate = useNavigate()

    const initialState = useSelector((state) => {
        return state.dashboard
    })

    const appUser = useSelector((state) => {
        return state['app-user']
    })

    /* ====================== onContentLoaded ===================== */

    useEffect(() => {
        dispatch(setLoading(true))
        dashboardService.getAllData().then((res) => {
            dispatch(setInitialData(res))
        }).catch(err => {
            dispatch(setLoading(false))
        })
    }, [location.pathname])

    /* ====================== functions ===================== */

    let handleModal = (status) => {
        setModal(status)
    }

    /* ====================== Modularized Components ===================== */

    const Container = () => {

        if (initialState?.isLoading) return <FullScreenLoader />
        else
            return (
                <div className="dashboard-page">
                    <Row className="row-sm">
                        <Col xl={9} sm={9} lg={12}>
                            <Row className="row-sm">
                                <OverviewTiles totalProjects={initialState.total_projects} petitioner={initialState.total_petitioner} beneficiary={initialState.total_beneficiary} />
                                <CaseGraphs graphsData={initialState.project_graph} />
                            </Row>
                        </Col>
                        <OpenCasesListView paralegalProjects={initialState?.open_project_para} />
                    </Row>
                    {/* Bottom - Custom Tiles */}
                    <CustomTileView />
                    {/* <!-- Row end --> */}
                </div>
            )
    }

    /* ====================== Component Render ===================== */

    return (
        <Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header={`Welcome ${appUser?.firstname}!`} BreadcrumbItemList={[{ name: "Dashboard" }]} />

            <Container />

            <Modal show={showModal} size="large">
                <Modal.Header
                    closeButton
                    onClick={() => {
                        handleModal(false)
                    }}
                >
                    <h6>PR Information & Status</h6>
                </Modal.Header>
                <Modal.Body>
                    {/* <h6>Modal Body</h6> */}
                    There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration.
                    <br />
                </Modal.Body>
                <Modal.Footer>
                    <Button
                        variant="primary"
                        onClick={() => {
                            handleModal(false)
                        }}
                        className="text-center"
                    >
                        Ok
                    </Button>
                    <Button
                        variant="danger"
                        onClick={() => {
                            handleModal(false)
                        }}
                        className="text-center"
                    >
                        Close
                    </Button>
                </Modal.Footer>
            </Modal>
            <Modal show={renameModal} size="md" backdrop="false">
                <Modal.Header closeButton onClick={() => setRenameModal(false)}>
                    <Modal.Title>Rename Tile</Modal.Title>
                </Modal.Header>
                <Modal.Body>{/* {tileRenameModalBody()} */}</Modal.Body>
                <Modal.Footer>
                    <Button variant="primary" onClick={() => setRenameModal(false)}>
                        Save Changes
                    </Button>
                    <Button variant="secondary" onClick={() => setRenameModal(false)}>
                        Close
                    </Button>
                </Modal.Footer>
            </Modal>
        </Fragment>
    )
}

Dashboard.propTypes = {}

Dashboard.defaultProps = {}

export default Dashboard
