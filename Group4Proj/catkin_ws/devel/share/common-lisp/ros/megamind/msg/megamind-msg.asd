
(cl:in-package :asdf)

(defsystem "megamind-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "CurrentGoal" :depends-on ("_package_CurrentGoal"))
    (:file "_package_CurrentGoal" :depends-on ("_package"))
  ))