import { defineStore } from "pinia";

export const useAuth = defineStore({
    id: "auth",
    state: () => ({
        user: {
            isAuthenticated: false,
            email: "",
            token: "",
        },
    }),

    actions: {
        initUser() {
            this.user.isAuthenticated = false;
            if(localStorage.getItem("user.token") && localStorage.getItem("user.email")) {
                this.user.isAuthenticated = true;
                this.user.email = localStorage.getItem("user.email");
                this.user.token = localStorage.getItem("user.token");
            }
        },

        login(email, token) {
            this.user.isAuthenticated = true;
            this.user.email = email;
            this.user.token = token;
            localStorage.setItem("user.email", email);
            localStorage.setItem("user.token", token);
        },

        logout() {
            this.user.isAuthenticated = false;
            this.user.email = "";
            this.user.token = "";
            if(localStorage.getItem("user.token") && localStorage.getItem("user.email")) {
                localStorage.removeItem("user.email");
                localStorage.removeItem("user.token");
            }
            navigateTo("/login");
        },
    },
});