import randomColor from "randomcolor"
import { useEffect } from "react"
import { Alert, Nav, Spinner } from "react-bootstrap"
import { useDispatch, useSelector } from "react-redux"
import { useLocation, useNavigate } from "react-router-dom"
import { petitionerService } from "services/petitioner.service"
import { actions } from "store/slices/petitionerSlice"
import { v4 as uuid } from "uuid"

export const SidePetitionerList = () => {

    const dispatch = useDispatch()
    const location = useLocation()
    const navigate = useNavigate()

    const initialState = useSelector((state) => {
        return state.petitioner
    })

    const loadAPI = () => {
        dispatch(actions.setPetitionerListLoading(true))
        petitionerService.getPetitionerList().then((res) => {

            if (!res)
                dispatch(actions.setPetitionerList([]))
            else
                dispatch(actions.setPetitionerList(res.petitioner))
        })
    }

    useEffect(() => {
        loadAPI()
    }, [location.pathname])

    const handleSelect = (id, name) => {
        dispatch(actions.setPetitionerInfo({ id, name }))

        navigate({
            pathname: './',
            search: `?pane=Overview&id=` + id,
        })

    }

    const ListItems = () => {

        if (initialState?.petitionerList.length === 0) {
            return (
                <div className="p-3 mt-3 text-center text-bold">
                    <i className="mdi mdi-alert-octagon h1"></i>
                    <h5>No Petitioner Assigned</h5>
                </div>
            )
        }

        return initialState?.petitionerList.map((list, index) => (
            <Nav.Item as="li" key={index}>
                <Nav.Link eventKey={0} className="d-flex align-items-center media" onClick={() => handleSelect(list.PetitionerID, list.PetitionerName)}>
                    <div className="me-2">
                        <div className="main-img-user">
                            <div style={{
                                    backgroundColor: randomColor({
                                        luminosity: "dark",
                                        format: "rgba",
                                        alpha: 0.3,
                                    }), color: "#3c4858", }}
                                className="avatar avatar-md d-none d-sm-flex">
                                {list.PetitionerName.charAt(0)}
                            </div>
                        </div>
                    </div>
                    <div className="align-items-center justify-content-between my-2">
                        <div className="media-body ms-2">
                            <div className="media-contact-name">
                                <strong>{list.PetitionerName}</strong>
                                <span></span>
                            </div>
                            <div className="d-flex align-items-center">
                                <p className="tx-13 mb-0">{list?.Desc}</p>
                            </div>
                        </div>
                    </div>
                </Nav.Link>
            </Nav.Item>
        ))
    }

    const LoadingState = () => {
        return (
            <Nav.Item key={uuid()}>
                <Alert className={`login-alert alert alert-primary text-start`} role="alert">
                    <Spinner animation="border" role="status">
                        <span className="visually-hidden"></span>
                    </Spinner>
                    <strong>Loading...</strong>
                </Alert>
            </Nav.Item>
        )
    }

    if (initialState?.isPetitionerListLoading) return <LoadingState />
    else return <ListItems />
}
