import { useSelector } from "react-redux"

const Permission = ({ allowedRoles, disallowedRoles, children }) => {
    // attorney
    // beneficiary
    // paralegal
    // hr
    // gm

    const appUser = useSelector((state) => {
        return state['app-user']
    })

    const current_user = { permission: appUser?.usertype?.toUpperCase() };
    
    // console.log(current_user)

    if (
        allowedRoles?.includes(current_user.permission) ||
        (!disallowedRoles?.includes(current_user.permission) &&
            !allowedRoles?.length)
    )
        return children;
};

export { Permission };