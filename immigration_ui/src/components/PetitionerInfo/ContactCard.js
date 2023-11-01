import { Card } from "react-bootstrap"

export const ContactCard = ({ data }) => {

    if(!data)
        return null

    return (
        <Card className="custom-card border rounded-5">
            <Card.Body>
                <div className="d-flex">
                    <div className="avatar avatar-md bg-primary-transparent text-primary">
                        <i className="ti-user fs-18"></i>
                    </div>
                    <div className="ms-3">
                        <p className="tx-13 mb-0 tx-semibold">Last Name</p>
                        <p className="tx-12 text-muted">{data.LastName}</p>
                    </div>
                </div>
                <div className="d-flex">
                    <div className="avatar avatar-md bg-primary-transparent text-primary">
                        <i className="ti-user fs-18"></i>
                    </div>
                    <div className="ms-3">
                        <p className="tx-13 mb-0 tx-semibold">First Name</p>
                        <p className="tx-12 text-muted">{data.FirstName}</p>
                    </div>
                </div>
                <div className="d-flex">
                    <div className="avatar avatar-md bg-primary-transparent text-primary">
                        <i className="ti-pencil-alt fs-18"></i>
                    </div>
                    <div className="ms-3">
                        <p className="tx-13 mb-0 tx-semibold">Job Title</p>
                        <p className="tx-12 text-muted">{data.JobTitle || 'NA'}</p>
                    </div>
                </div>
                <div className="d-flex">
                    <div className="avatar avatar-md bg-primary-transparent text-primary">
                        <i className="ti-mobile fs-18"></i>
                    </div>
                    <div className="ms-3">
                        <p className="tx-13 mb-0 tx-semibold">Phone</p>
                        <p className="tx-12 text-muted">{data.Phone}</p>
                    </div>
                </div>
                <div className="d-flex">
                    <div className="avatar avatar-md bg-primary-transparent text-primary">
                        <i className="ti-email fs-18"></i>
                    </div>
                    <div className="ms-3">
                        <p className="tx-13 mb-0 tx-semibold">Email</p>
                        <p className="tx-12 text-muted mb-0">{data.Email}</p>
                    </div>
                </div>
            </Card.Body>
        </Card>
    )
}
