
(cl:in-package :asdf)

(defsystem "megamind-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Decision" :depends-on ("_package_Decision"))
    (:file "_package_Decision" :depends-on ("_package"))
  ))