import { SimpleLoader } from "components/Common/SimpleLoader"
import randomColor from "randomcolor"
import { Card, Nav, Row } from "react-bootstrap"
import { useSelector } from "react-redux"
import { useNavigate, useSearchParams } from "react-router-dom"

export function ProfileSection() {

    const navigate = useNavigate()

    const initialState = useSelector((state) => {
        return state.petitioner.profileData
    })

    const tabChange = (name) => {

        navigate({
            pathname: './',
            search: `?pane=${name}`,
        })
    }

    const ProfileCover = () => {

        return <div className="panel profile-cover">
            <div className="profile-cover__img">
                <img src={require("../../assets/img/users/1.jpg")} alt="img" />
                <h3 className="h3">{initialState.petitionerName}</h3>
            </div>
            <div className="profile-cover__action bg-img" style={{ background: "linear-gradient(90deg," + randomColor() + " 0%, " + randomColor() + " 100%)"}}></div>
            <div className="profile-tab" style={{marginTop: "6rem"}}>
                <Nav variant="pills" className="p-2 bg-primary-transparent rounded-5">
                    <Nav.Item>
                        <Nav.Link eventKey="Overview" className="mx-3" onClick={() => tabChange('Overview')}>
                            Overview
                        </Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Nav.Link eventKey="Incorporation" className="mx-3" onClick={() => tabChange('Incorporation')}>
                            Incorporation Data
                        </Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Nav.Link eventKey="Employee" className="mx-3" onClick={() => tabChange('EmployeeRevenue')}>
                            Employee & Revenue Data
                        </Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Nav.Link eventKey="Immigration" className="mx-3" onClick={() => tabChange('Immigration')}>
                            Immigration Data
                        </Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Nav.Link eventKey="Authorized" className="mx-3" onClick={() => tabChange('AuthorizedSignatoryInfo')}>
                            Authorized Signatory Info
                        </Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Nav.Link eventKey="Contact" className="mx-3" onClick={() => tabChange('Contact')}>
                            Contact Info
                        </Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Nav.Link eventKey="DMSWorkspaceLink" className="mx-3" onClick={() => tabChange('DMSWorkspaceLink')}>
                            DMS Workspace Link
                        </Nav.Link>
                    </Nav.Item>
                </Nav>
            </div>
        </div>
    }

    return initialState?.petitionerID === 0 ? null : (
        <Row className="square">
            <Card className="custom-card">
                <Card.Body style={{ padding: "15px" }}>
                    <ProfileCover />
                </Card.Body>
            </Card>
        </Row>
    )
}
