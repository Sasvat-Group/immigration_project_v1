import { configureStore } from "@reduxjs/toolkit"
import commonReducer from "store/slices/commonSlice"
import storage from "redux-persist/lib/storage"
import { persistReducer } from "redux-persist"
import { combineReducers } from "@reduxjs/toolkit"

import dashboardReducer from "store/slices/dashboardSlice"
import petitionerReducer from "store/slices/petitionerSlice"
import caseProcessReducer from "store/slices/caseProcessSlice"
import beneficiaryReducer from "store/slices/beneficiarySlice"
import appUserSlice from "store/slices/userSlice"

const persistConfig = {
    key: "root",
    version: 1,
    whitelist: ['app-user'],
    storage
}

const reducer = combineReducers({
    "common": commonReducer,
    "dashboard": dashboardReducer,
    "petitioner": petitionerReducer,
    "case-process": caseProcessReducer,
    "beneficiary": beneficiaryReducer,
    "app-user": appUserSlice,
})

const persistedReducer = persistReducer(persistConfig, reducer)

const store = configureStore({
    reducer: persistedReducer,
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware({
            serializableCheck: false,
        }),
})

export { store }
